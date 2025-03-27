#------------TO RUN: in git bash terminal, type "flask --app finalproject run"----------------
from flask import Flask as fl

app = fl(__name__)

@app.route("/")

def hello_world():
    return "<p> Hello, world! </p>"