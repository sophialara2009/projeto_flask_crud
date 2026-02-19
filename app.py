# app.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return "<h1>Olá Mundo"

if __name__ == '__main__':
    app.run(debug=True)