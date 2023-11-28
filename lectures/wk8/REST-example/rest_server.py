"""
A basic Flask setup. Run this file as a normal Python file, then use the IP
address 127.0.0.1 in the browser to display. Alternatively, use the command
FLASK_APP=a_server (or whatever the filename is), then the command 'flask run'.
"""
from flask import Flask, abort, jsonify, redirect, request, url_for

app = Flask(__name__, static_url_path='', static_folder='static')


@app.route('/')
def index():
    """Function for default URL, returns link from another function."""
    return "hello"


if __name__ == '__main__':
    app.run(debug=True)
