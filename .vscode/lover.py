from flask import Flask, render_template
import flask

app = flask.Flask(__name__)


@app.route("/")
def home():
    return render_template("lover.html")


if __name__ == "__main__":
    app.run(debug=True)