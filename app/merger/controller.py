from re import T
from flask.helpers import flash, get_flashed_messages, send_file, url_for
from flask.templating import render_template
from werkzeug.utils import secure_filename
from app import merger
from flask import Blueprint, request, current_app, redirect, after_this_request
import os
import time
from ..pdfTools import details, merger
from ..utils import metadata
import shutil


merger_blueprint = Blueprint('merger', __name__, url_prefix="/merger",
                             static_folder="../static", template_folder="../templates/merger")


@merger_blueprint.route('/')
def index():
    curr_time = int(time.time())
    print('index')
    return render_template('merger.html.j2', id=curr_time)


@merger_blueprint.route('<folderid>/upload', methods=['GET', 'POST'])
def upload(folderid):
    get_flashed_messages()
    folder = current_app.config['UPLOAD_FOLDER'] + folderid
    if request.method == 'POST':
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
    folder = current_app.config['UPLOAD_FOLDER'] + folderid
    files_dict = dict()
    file_list = []
    try:
        for filename in os.listdir(folder):
            # print(details.get_page_numbers(folder, filename))
            file_list.append({
                "filename": filename,
                "pages": details.get_page_numbers(folder, filename)
            })
    except Exception:
        flash("Please upload atleast ONE file!")
        return redirect(url_for('merger.upload', folderid=folderid))

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

        folder = current_app.config['UPLOAD_FOLDER'] + folderid
        merger.merge(ordered_file_list, folder, folderid+".pdf")

    return render_template("complete.html.j2", id=folderid)


@merger_blueprint.route('<folderid>/download/')
def download(folderid):
    folder = current_app.config['UPLOAD_FOLDER'] + folderid
    download_file = os.path.join(folder, folderid + ".pdf")
    file_handle = open(download_file, 'rb')

    def generate():
        yield from file_handle
        file_handle.close()
        # os.remove(folder)
        # shutil.rmtree(folder, ignore_errors=True)
        for filename in os.listdir(folder):
            filepath = os.path.join(folder, filename)
            try:
                shutil.rmtree(filepath)
            except OSError:
                os.remove(filepath)
        shutil.rmtree(folder, ignore_errors=True)

    r = current_app.response_class(generate(), mimetype='application/pdf')
    r.headers.set('Content-Disposition', 'attachment',
                  filename=folderid + '.pdf')
    return r
    # return send_file(download_file, as_attachment=True, cache_timeout=0)
