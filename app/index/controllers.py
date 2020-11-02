from flask import Blueprint
from flask.templating import render_template

index_blueprint = Blueprint('index', __name__, url_prefix="/",
                            static_folder="../static", template_folder="../templates/index")


@index_blueprint.route('/')
def index():
    return render_template("index.html.j2")
