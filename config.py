import time


class Config():
    SECRET_KEY = "This is super duper secret stuff!"
    UPLOAD_FOLDER = 'uploads/'


class DevConfig(Config):
    DEBUG = True
    TIME_LIMIT = 3600


class ProdConfig(Config):
    TIME_LIMIT = 600


class LocalConfig(Config):
    TIME_LIMIT = False
