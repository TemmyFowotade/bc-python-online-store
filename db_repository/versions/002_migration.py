from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
products = Table('products', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('productname', String(length=64), nullable=False),
    Column('productdescription', String(length=140), nullable=False),
    Column('productprice', Integer, nullable=False),
    Column('productquantity', Integer, nullable=False),
    Column('store_id', Integer, nullable=False),
)

stores = Table('stores', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('storename', String(length=64), nullable=False),
    Column('storeurl', String(length=64), nullable=False),
    Column('storedescription', String(length=120), nullable=False),
    Column('storeaddress', String(length=120), nullable=False),
    Column('storecity', String(length=64), nullable=False),
    Column('storestate', String(length=64), nullable=False),
    Column('user_id', Integer, nullable=False),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['products'].create()
    post_meta.tables['stores'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['products'].drop()
    post_meta.tables['stores'].drop()
