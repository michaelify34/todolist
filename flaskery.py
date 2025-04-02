#------------TO RUN: in git bash terminal, type "flask --app {filename} run"----------------
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("main.html")

if __name__ == "__main__":
    app.run(debug=True)