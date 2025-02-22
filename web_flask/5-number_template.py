#!/usr/bin/python3
"""This module starts a Flask web application that will be served
   in 'http://0.0.0.0:5000/'"""

from flask import Flask, render_template

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays string"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays string"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def show_c_var(text):
    """display C followed by the value of the text variable and
    replace underscore _ symbols with a space"""
    str_without_sym = text.replace('_', ' ')
    return 'C %s' % str_without_sym


@app.route("/number/<int:n>", strict_slashes=False)
def show_python_var(n):
    """display n is a number only if n is an integer"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def n_template(n):
    """display a HTML page only if n is an integer
    and will be return a html file with the integer"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
