#!flask/bin/python
from migrate.versioning import api
from config import config
v = api.db_version(config['development'].SQLALCHEMY_DATABASE_URI, config['development'].SQLALCHEMY_MIGRATE_REPO)
api.downgrade(config['development'].SQLALCHEMY_DATABASE_URI, config['development'].SQLALCHEMY_MIGRATE_REPO, v - 1)
v = api.db_version(config['development'].SQLALCHEMY_DATABASE_URI, config['development'].SQLALCHEMY_MIGRATE_REPO)
print('Current database version: ' + str(v))
