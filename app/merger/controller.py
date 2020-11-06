from re import T
from flask.ctx import copy_current_request_context
from flask.helpers import flash, get_flashed_messages, send_file, url_for
from flask.templating import render_template
from werkzeug.utils import secure_filename
from app import merger
from flask import Blueprint, request, current_app, redirect, after_this_request
import os
import time
from ..pdfTools import details, merger
from ..utils import metadata, checksession
import shutil
import threading


merger_blueprint = Blueprint('merger', __name__, url_prefix="/merger",
                             static_folder="../static", template_folder="../templates/merger")


class cleanupThread(threading.Thread):
    def __init__(self, root, threadID):
        threading.Thread.__init__(self)
        self.root = root
        self.threadID = threadID
        self.start_time = time.time()

    def run(self):
        print("cleanupThread WAITING for threadID: {} started...!".format(self.threadID))
        time.sleep(660)
        print("cleanupThread CLEANUP for threadID: {} started...!".format(self.threadID))
        self.cleanup(self.root, self.threadID)
        print("cleanupThread for threadID: {} ended...!".format(self.threadID))

    @staticmethod
    def cleanup(root, id):
        new_open_file_list = []
        for openfile in merger.openfile_list:
            if openfile['id'] == id:
                openfile['file'].close()
            else:
                new_open_file_list.append(openfile)
        merger.openfile_list = new_open_file_list

        folder = os.path.join(root, id)

        if os.path.exists(folder):
            for filename in os.listdir(folder):
                filepath = os.path.join(folder, filename)
                try:
                    shutil.rmtree(filepath)
                except OSError:
                    os.remove(filepath)
        shutil.rmtree(folder, ignore_errors=True)


@merger_blueprint.route('/')
def index():
    curr_time = int(time.time())
    print('index')
    return render_template('merger.html.j2', id=curr_time)


@merger_blueprint.route('<folderid>/upload/', methods=['GET', 'POST'])
def upload(folderid):
    if not checksession.check_session_timestamp(folderid):
        return render_template('expire.html.j2')

    get_flashed_messages()
    folder = current_app.config['UPLOAD_FOLDER'] + folderid

    if request.method == 'POST':
        ct = cleanupThread(current_app.config['UPLOAD_FOLDER'], folderid)
        ct.start()

        if not os.path.exists(folder):
            os.makedirs(folder)

        count = 0
        for key, f in request.files.items():
            if key.startswith('file'):
                if f.filename.endswith('.pdf'):
                    f.save(os.path.join(folder, f.filename))
                    print("Uploaded...", f.filename)
                    count += 1
                else:
                    print("Not a .pdf file!")
                    return render_template('upload.html.j2', id=folderid)
        if count == 0:
            print("No files uploaded!")
            return render_template('upload.html.j2', id=folderid)

        return render_template('arrange.html.j2', id=folderid)
    else:
        return render_template('upload.html.j2', id=folderid)


@merger_blueprint.route('<folderid>/arrange/',  methods=['GET', 'POST'])
def arrange(folderid):
    folder = os.path.join(current_app.config['UPLOAD_FOLDER'], folderid)
    files_dict = dict()
    file_list = []
    print(os.listdir(folder))
    try:
        for filename in os.listdir(folder):
            file_list.append({
                "filename": filename,
                "pages": details.get_page_numbers(folder, filename)
            })
    except Exception:
        print("Please upload atleast ONE file!")
        return redirect(url_for('merger.index'))

    print(file_list)

    return render_template('arrange.html.j2', file_list=file_list, id=folderid)


@merger_blueprint.route('<folderid>/complete/', methods=['GET', 'POST'])
def complete(folderid):
    if request.method == 'POST':
        print(request.form)

        ordered_file_list = metadata.build_metadata(request.form)

        print(ordered_file_list)
        if len(ordered_file_list) == 0:
            print(request.referrer)
            return redirect("/merger/" + folderid + "/arrange/")

        folder = os.path.join(current_app.config['UPLOAD_FOLDER'], folderid)
        merger.merge(ordered_file_list, folder, folderid+".pdf")

        print(merger.openfile_list)

    return render_template("complete.html.j2", id=folderid)


@merger_blueprint.route('<folderid>/download/')
def download(folderid):
    folder = os.path.join(current_app.config['UPLOAD_FOLDER'], folderid)
    download_file = os.path.join(folder, folderid + ".pdf")
    file_handle = open(download_file, 'rb')
    root = current_app.config['UPLOAD_FOLDER']

    def generate():
        yield from file_handle
        file_handle.close()
        cleanupThread.cleanup(root, folderid)

    r = current_app.response_class(generate(), mimetype='application/pdf')
    r.headers.set('Content-Disposition', 'attachment',
                  filename=folderid + '.pdf')
    return r


@merger_blueprint.route('session-expired/')
def expired():
    return render_template('expire.html.j2')
