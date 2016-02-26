#!flask/bin/python
from migrate.versioning import api
from config import config
api.upgrade(config['development'].SQLALCHEMY_DATABASE_URI, config['development'].SQLALCHEMY_MIGRATE_REPO)
v = api.db_version(config['development'].SQLALCHEMY_DATABASE_URI, config['development'].SQLALCHEMY_MIGRATE_REPO)
print('Current database version: ' + str(v))
