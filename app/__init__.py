from flask import Flask, render_template
# from config import DevConfig


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_name)

    from .index.controllers import index_blueprint
    app.register_blueprint(index_blueprint)

    return app
