from flask import Flask, render_template
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