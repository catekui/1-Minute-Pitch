from flask import Flask, render_template, url_for
from app import app
from forms import RegistrationForm, LoginForm

app.config['SECRET_KEY'] = 'c2b68daba34ee09a4cdea2f1d76be4e6'

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
        'content':'Intellectual skills can be cultivated',
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

@app.route('/register')
def register ():
    form = RegistrationForm()
    return render_template('register.html',title='Register', form=form)

@app.route('/login')
def login ():
    form = LoginForm()
    return render_template('register.html',title='Login', form=form)