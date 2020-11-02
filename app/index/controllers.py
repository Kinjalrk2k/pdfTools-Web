from flask import Blueprint

index_blueprint = Blueprint('index', __name__, url_prefix="/")


@index_blueprint.route('/')
def index():
    return "Hello, Kinjal!"
