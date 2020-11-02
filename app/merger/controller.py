from flask.templating import render_template
from werkzeug.utils import secure_filename
from app import merger
from flask import Blueprint, request, current_app
import os
import time

merger_blueprint = Blueprint('merger', __name__, url_prefix="/merger",
                             static_folder="../static", template_folder="../templates/merger")


@merger_blueprint.route('/')
def index():
    return render_template('index.html.j2')


@merger_blueprint.route('/upload', methods=['GET', 'POST'])
def upload():
    folder = current_app.config['UPLOAD_FOLDER'] + str(int(time.time()))
    if request.method == 'POST':
        if not os.path.exists(folder):
            os.makedirs(folder)
        f = request.files.get('file')
        filename = secure_filename(f.filename)
        f.save(os.path.join(folder, filename))

    return render_template('upload.html.j2')
