#------------TO RUN: in git bash terminal, type "flask --app {filename} run"----------------
from flask import Flask as fl

app = fl(__name__)

@app.route("/")

@app.route("/home")
def home():
    return "<h1> To-Do List </h1>"