from flask import Flask, request, redirect, url_for, render_template
from blog import app, db

@app.route('/')
def homepage():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)