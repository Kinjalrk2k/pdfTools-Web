from flask import Flask, render_template
# from config import DevConfig
from flask_dropzone import Dropzone

dropzone = Dropzone()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_name)

    dropzone.init_app(app)

    from .index.controllers import index_blueprint
    app.register_blueprint(index_blueprint)

    from .merger.controller import merger_blueprint
    app.register_blueprint(merger_blueprint)

    return app
