# -*-coding: utf-8 -*-

from flaskr2 import app

@app.route("/greet1")
def greet1():
    return "Hello, world no.1¥n"
