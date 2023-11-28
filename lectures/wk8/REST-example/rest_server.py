"""
A basic Flask setup. Run this file as a normal Python file, then use the IP
address 127.0.0.1 in the browser to display. Alternatively, use the command
FLASK_APP=a_server (or whatever the filename is), then the command 'flask run'.
"""
from flask import Flask


# abort, jsonify, redirect, request, url_for

app = Flask(__name__, static_url_path='', static_folder='static')


@app.route('/')
def index():
    """Function for default URL, returns link from another function."""
    return "hello"


@app.route('/books')
def get_all():
    """Return all books."""
    return "served by getAll"


@app.route('/books/<int:id>')
def find_by_id(id):
    """Return a book."""
    return "served by findByID" + str(id)


@app.route('/books', methods=['POST'])
def create_book():
    """POSTs a book via JSON. Note that browsers can only test GET requests,
    if you want to test this POST you can use the following command in cmd:
        curl -X POST http://127.0.0.1:5000/books"""
    return "served by create_book"


@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    """PUTs a book via JSON. This can be tested using the method described
    in the create_book route. """
    return "served by update_book " + str(id)


@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    """DELETEs a book using a given ID."""
    return "served by delete_book " + str(id)


if __name__ == '__main__':
    app.run(debug=True)
