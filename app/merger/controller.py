from re import T
from flask.helpers import send_file, url_for
from flask.templating import render_template
from werkzeug.utils import secure_filename
from app import merger
from flask import Blueprint, request, current_app, redirect
import os
import time
from ..pdfTools import details, merger


merger_blueprint = Blueprint('merger', __name__, url_prefix="/merger",
                             static_folder="../static", template_folder="../templates/merger")


@merger_blueprint.route('/')
def index():
    curr_time = int(time.time())
    print('index')
    return render_template('merger.html.j2', id=curr_time)


@merger_blueprint.route('<folderid>/upload', methods=['GET', 'POST'])
def upload(folderid):
    folder = current_app.config['UPLOAD_FOLDER'] + folderid
    if request.method == 'POST':
        if not os.path.exists(folder):
            os.makedirs(folder)

        for key, f in request.files.items():
            if key.startswith('file'):
                f.save(os.path.join(folder, f.filename))
                print("Uploaded...", f.filename)
        return render_template('arrange.html.j2', id=folderid)
    else:
        return render_template('upload.html.j2', id=folderid)


@merger_blueprint.route('<folderid>/arrange/',  methods=['GET', 'POST'])
def arrange(folderid):
    folder = current_app.config['UPLOAD_FOLDER'] + folderid
    files_dict = dict()
    file_list = []
    for filename in os.listdir(folder):
        # print(details.get_page_numbers(folder, filename))
        file_list.append({
            "filename": filename,
            "pages": details.get_page_numbers(folder, filename)
        })

    print(file_list)

    return render_template('arrange.html.j2', file_list=file_list, id=folderid)


def ordered_dict_yielder(ordered_dict):
    for key, values in ordered_dict.items():
        yield values


@merger_blueprint.route('<folderid>/complete/', methods=['GET', 'POST'])
def complete(folderid):
    if request.method == 'POST':
        print(request.form)

        i = 0
        ignore = False
        temp_dict = dict()
        ordered_file_list = []

        # for i, value in enumerate(ordered_dict_yielder(request.form)):
        #     print(i, value)
        #     print(ordered_dict_yielder(request.form))

        for key, value in request.form.items():
            print(i, key, value)
            if i == 0:
                if value == "on":
                    ignore = False
                    # i += 1
                else:
                    ignore = True
                    i += 1
            if i == 1 and (not ignore):
                temp_dict["filename"] = value
                # i += 1
            elif i == 2 and (not ignore):
                temp_dict["start"] = int(value)
                # i += 1
            elif i == 3:
                if not ignore:
                    temp_dict["end"] = int(value)
                    print(temp_dict)
                    ordered_file_list.append(temp_dict.copy())
                i = 0
                ignore = False
                continue
            i += 1

        print(ordered_file_list)
        folder = current_app.config['UPLOAD_FOLDER'] + folderid
        merger.merge(ordered_file_list, folder, folderid+".pdf")

    return render_template("complete.html.j2", id=folderid)


@merger_blueprint.route('<folderid>/download/')
def download(folderid):
    folder = current_app.config['UPLOAD_FOLDER'] + folderid
    download_file = os.path.join("..", folder, folderid + ".pdf")

    return send_file(download_file, as_attachment=True)
