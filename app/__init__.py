from flask import Flask, render_template, Request
from flask.helpers import url_for
from werkzeug.utils import redirect
from config import DevConfig as CurrentConfig
from flask_dropzone import Dropzone

from werkzeug.datastructures import ImmutableOrderedMultiDict


class MyRequest(Request):
    parameter_storage_class = ImmutableOrderedMultiDict


class MyFlask(Flask):
    request_class = MyRequest


dropzone = Dropzone()


def create_app():
    app = MyFlask(__name__)
    app.config.from_object(CurrentConfig)

    dropzone.init_app(app)

    from .index.controllers import index_blueprint
    app.register_blueprint(index_blueprint)

    from .merger.controller import merger_blueprint
    app.register_blueprint(merger_blueprint)

    from .errors.controller import error_blueprint
    app.register_blueprint(error_blueprint)
    # app.register_error_handler(error_blueprint)

    return app
