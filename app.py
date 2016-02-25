from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps

app = Flask(__name__)

app.secret_key = 'my-personal-key'

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

def login_required(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['email'] != 'admin' or request.form['password'] != 'admin':
            error = "Invalid credentials"
        else:
            session['logged_in'] = True
            return redirect(url_for('create_store'))
    return render_template('login.html', error=error)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        if request.form['email'] != 'admin' or request.form['password'] != 'admin':
            error = "Invalid credentials"
        else:
            session['logged_in'] = True
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