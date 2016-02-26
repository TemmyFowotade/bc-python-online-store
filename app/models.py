#database file using flask sqlalchemy-->
from app import db


class User(db.Model):
    """Database table for users, having a one to one relationship with the Store database.

    Args: 
    db.Model initialized from sqlalchemy
    """

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password = db.Column(db.String(64), index=True, nullable=False)
    store = db.relationship('Store', uselist=False, backref='owner')

    """generated from flask login.
    checks if user is in authenticated mode.
    """
    @property
    def is_authenticated(self):
        return True


    """generated from flask login.
    checks if user is in active mode.
    """ 
    @property
    def is_active(self):
        return True


    """generated from flask login.
    checks if user is fake.
    """    
    @property
    def is_anonymous(self):
        return False


    """generated from flask login.
    checks for compatibility with different versions of python.
    """
    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % (self.username)


class Store(db.Model):
     """Database table for stores, having a one to one relationship with the User database and a one-to-many relationship
     with the product database.

    Args: 
    db.Model initialized from sqlalchemy
    """

    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key = True)
    storename = db.Column(db.String(64), index=True, nullable=False)
    storeurl = db.Column(db.String(64), index=True, nullable=False)
    storedescription = db.Column(db.String(120), index=True, nullable=False)
    storeaddress = db.Column(db.String(120), index=True, nullable=False)
    storecity = db.Column(db.String(64), index=True, nullable=False)
    storestate = db.Column(db.String(64), index=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    product = db.relationship('Product', backref='store', lazy='dynamic', cascade="all, delete-orphan")

    def __repr__(self):
        return '<Store %r>' % (self.storename)


class Product(db.Model):
     """Database table for products, having a many to one relationship with the Store database.

    Args: 
    db.Model initialized from sqlalchemy
    """

    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    productname = db.Column(db.String(64), index=True, nullable=False)
    productdescription = db.Column(db.String(140), index=True, nullable=False)
    productprice = db.Column(db.Integer, index=True, nullable=False)
    productquantity = db.Column(db.Integer, index=True, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'), nullable=False)
    

    def __repr__(self):
        return '<Product %r>' % (self.productname)