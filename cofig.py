import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    STRICT_SLASHES = False



class TestingConfig(BaseConfig):
    TESTING = True


class DevelopmentConfig(BaseConfig):
    DEBUG = True
