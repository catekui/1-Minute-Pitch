from flask import Flask, render_template, url_for, flash, redirect
from app.models import *
from app.forms import RegistrationForm, LoginForm
from app import app

quotes = [
    {
        'author': 'Sweet Cate',
        'title': 'Quote No 1',
        'content':'Intellectual skills can be cultivated',
        'date_posted': 'May 7, 2022'
    },
    {
        'author': 'Ann Wamuya',
        'title': 'Qoute No 2',
        'content':'No Human is limited',
        'date_posted': 'May 8, 2022'
    }
]
@app.route('/')
@app.route('/home')
def home ():
    return render_template('home.html', quotes=quotes)

@app.route('/about')
def about ():
    return render_template('about.html', title='About')

@app.route('/register', methods=['POST', 'GET'])
def register ():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)