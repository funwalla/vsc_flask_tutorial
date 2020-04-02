# VS Code Flask Tutorials
# https://code.visualstudio.com/docs/python/tutorial-flask
#
# Added template for page rendering
# Refer to static files in a template

from flask import Flask
from flask import render_template
from datetime import datetime
import re

app = Flask(__name__)
@app.route("/")
def home():
    return "Hello Flask"

@app.route("/hello/<name>")
def hello_there(name=None):
     return render_template(
         "hello_there.html",
         name=name,
         date=datetime.now()
     )
