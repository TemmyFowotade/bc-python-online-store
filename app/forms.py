from flask_wtf import Form
from wtforms import TextField, PasswordField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(Form):
    email = TextField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
  
class RegisterForm(Form):
    username = TextField(
        'username',
        validators=[DataRequired(), Length(min=3, max=25)]
    )
    email = TextField(
        'email',
        validators=[DataRequired(), Email(message=None), Length(min=6, max=40)]
    )
    password = PasswordField(
        'password',
        validators=[DataRequired(), Length(min=6, max=25)]
    )
    confirm = PasswordField(
        'Repeat password',
        validators=[
            DataRequired(), EqualTo('password', message='Passwords must match.')
        ]
    )

class CreateStoreForm(Form):
    storename = TextField(
        'storename',
        validators=[DataRequired(), Length(min=3, max=25)]
    )
    storeurl = TextField(
        'storeurl',
        validators=[DataRequired(), Length(min=3, max=25)]
    )
    storedescription = TextField(
        'storedescription',
        validators=[DataRequired(), Length(min=25, max=125)]
    )
    storeaddress = TextField(
        'storeaddress',
        validators=[DataRequired(), Length(min=3, max=25)]
    )
    storecity = TextField(
        'storecity',
        validators=[DataRequired(), Length(min=3, max=25)]
    )
    storestate = TextField(
        'storestate',
        validators=[DataRequired(), Length(min=3, max=25)]
    )

class CreateProduct(Form):
    productname = TextField(
        'productname',
        validators=[DataRequired(), Length(min=3, max=25)]
    )
    productdescription = TextField(
        'productdescription',
        validators=[DataRequired(), Length(min=3, max=25)]
    )
    productprice = DecimalField(
        'productprice',
        validators=[DataRequired(), Length(min=3, max=10)]
    )
    productquantity = IntegerField(
        'productquantity',
        validators=[DataRequired(), Length(min=3, max=10)]
    )





