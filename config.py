import os
basedir = os.path.abspath(os.path.dirname(__file__))


# default config
class BaseConfig(object):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = 'very-secret'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')



class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SECRET_KEY = os.getenv('SECRET_KEY')

config = {
    'development': DevelopmentConfig,
    'testing': TestConfig,
    'production': ProductionConfig
}