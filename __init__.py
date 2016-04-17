# -*-coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "This is index."

from flaskr2.myapp import file1
from flaskr2.myapp import file2
