from flask import render_template, redirect, url_for, request, session, flash
from flask.ext.login import login_user, login_required, logout_user
from app import app, db, lm
from .models import *
from .forms import LoginForm, RegisterForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(email=request.form['email']).first()
            if user and request.form['password'] == user.password:
                login_user(user)
                return redirect(url_for('create_store'))
            else:
                error = 'Invalid username or password.'
    return render_template('login.html', error=error, form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('create_store'))
    return render_template('signup.html', form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/create_store', methods=['GET', 'POST'])
@login_required
def create_store():
    if request.method == 'POST':
        form = CreateProduct()
        if form.validate_on_submit():
            store = Store(
            storename = form.storename.data,
            storeurl = 
            storedescription = form.storedescription.data,
            storeaddress = form.storeaddress.data,
            storecity = form.storecity.data,
            storestate = form.storeaddress.data,
            )

        return redirect(url_for('dashboard'))
    return render_template('create_store.html')


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')



if __name__ == '__main__':
    app.run(debug=True)