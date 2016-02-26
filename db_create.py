#!flask/bin/python
from migrate.versioning import api
from config import config
from app import db
import os.path
db.create_all()
if not os.path.exists(config['development'].SQLALCHEMY_MIGRATE_REPO):
    api.create(config['development'].SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(config['development'].SQLALCHEMY_DATABASE_URI, config['development'].SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(config['development'].SQLALCHEMY_DATABASE_URI, config['development'].SQLALCHEMY_MIGRATE_REPO,
                        api.version(config['development'].SQLALCHEMY_MIGRATE_REPO))
