from flask import render_template, request
from application import app


@app.route('/')
def index():
    return render_template('home.html')