from flask.templating import render_template
from app import merger
from flask import Blueprint, request
import os

merger_blueprint = Blueprint('merger', __name__, url_prefix="/merger",
                             static_folder="../static", template_folder="../templates/merger")


@merger_blueprint.route('/')
def index():
    return render_template('index.html.j2')


@merger_blueprint.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if not os.path.exists('uploads'):
            os.makedirs('uploads')
        f = request.files.get('file')
        f.save(os.path.join('uploads', f.filename))

    return render_template('upload.html.j2')
