import time


class Config():
    SECRET_KEY = "This is super duper secret stuff!"
    UPLOAD_FOLDER = 'uploads/'


class DevConfig(Config):
    DEBUG = True
