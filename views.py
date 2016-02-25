from flask import render_template, redirect, url_for, request, session, flash, g
from flask.ext.login import login_user, login_required, logout_user
from app import app
from models import *
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
            if user is not None and password == user.password:
                login_user(user)
                return redirect(url_for('create_store'))
            else:
                error = 'Invalid username or password.'
    return render_template('login.html', error=error, form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User(email = email, password = password)
        
        if email != '' password != '':
            error = "Please fill all fields to login"
        else:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('create_store'))
    return render_template('signup.html', error=error)


@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))


@app.route('/create_store', methods=['GET', 'POST'])
@login_required
def create_store():
    if request.method == 'POST':
        return redirect(url_for('dashboard'))
    return render_template('create_store.html')


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')



if __name__ == '__main__':
    app.run(debug=True)