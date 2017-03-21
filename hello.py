from flask import Flask, url_for, render_template
from jinja2 import Markup

app = Flask(__name__)

@app.route('/')
def index():
    return 'Zde najdes moudro sveta'

@app.route('/hello/')
@app.route('/hello/<name>/')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/hello/<username>/<int:count>/')
def profile(username,count):
    return 'Hello {} <br>'.format(username)* count


@app.template_filter
def reverse(text):
    return reversed(text)

@app.template_filter('em')
def em(text):
    return Markup('<em>{}</em>').format(text)
