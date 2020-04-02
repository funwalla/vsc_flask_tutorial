# VS Code Flask Tutorials
# Use a template to render a page
# https://code.visualstudio.com/docs/python/tutorial-flask#_use-a-template-to-render-a-page

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
