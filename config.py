class Config():
    SECRET_KEY = "This is super duper secret stuff!"


class DevConfig(Config):
    DEBUG = True
