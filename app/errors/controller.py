from re import error
from flask import Blueprint
from flask.templating import render_template
# from app import app

error_blueprint = Blueprint(
    "error", __name__, static_folder="../static", template_folder="../templates/errors")


@error_blueprint.app_errorhandler(404)
def page_not_found(e):
    return render_template("error.html.j2", code=404, message="How dare you break the code...?"), 404


@error_blueprint.app_errorhandler(500)
def page_not_found(e):
    return render_template("error.html.j2", code=500, message="The server got annoyed...!"), 500
