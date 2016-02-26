import os
basedir = os.path.abspath(os.path.dirname(__file__))


# default config
class BaseConfig(object):
    """Basic configuration for the app.
    """

    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = 'very-secret'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')



class TestConfig(BaseConfig):
    """App configuration while on testing environment.
    """

    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class DevelopmentConfig(BaseConfig):
    """App configuration while on development environment.
    """

    DEBUG = True


class ProductionConfig(BaseConfig):
    """App configuration while on production environment.
    """

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SECRET_KEY = os.getenv('SECRET_KEY')

config = {
    """config object to enable easy access to the different environment."""
    'development': DevelopmentConfig,
    'testing': TestConfig,
    'production': ProductionConfig
}