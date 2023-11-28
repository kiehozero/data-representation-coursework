"""
A basic Flask setup. Run this file as a normal Python file, then use the IP
address 127.0.0.1 in the browser to display. Alternatively, use the command
FLASK_APP=a_server (or whatever the filename is), then the command 'flask run'.
"""
from flask import abort, Flask, jsonify, request

# redirect, url_for

app = Flask(__name__, static_url_path='', static_folder='static')

books = [
    {"id": 1, "title": "from the", "author": "bogs of", "price": 21},
    {"id": 2, "title": "big bill", "author": "ilya bryzgalov", "price": 21},
    {"id": 3, "title": "fod", "author": "phil foden", "price": 21},
]


nextId = 4


@app.route('/')
def index():
    """Function for default URL, returns link from another function."""
    return "hello"


@app.route('/books')
def get_all():
    """Return all books."""
    return jsonify(books)


@app.route('/books/<int:id>')
def find_by_id(id):
    """Return a book."""
    found_books = list(filter(lambda t: t["id"] == id, books))
    if len(found_books) == 0:
        # added a status code here just as a reminder that you can do it.
        return jsonify({}), 204
    return jsonify({found_books[0]})


@app.route('/books', methods=['POST'])
def create_book():
    """POSTs a book via JSON. Note that browsers can only test GET requests,
    if you want to test this POST you can use the following command in cmd:
        curl -X POST -H "content-type: application/json" -d "{\"title\":\"test
        curl\", \"author\":\"simone de beauvoir\", \"price\":123}"
       POST http://127.0.0.1:5000/books"""
    global nextId

    if not request.json:
        abort(400)

    book = {
        "id": nextId,
        "title": request.json["title"],
        "author": request.json["author"],
        "price": request.json["price"]
    }
    books.append(book)
    nextId += 1
    return jsonify(book)


@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    """PUTs a book via JSON. This can be tested using the method described
    in the create_book route. This recycles code from find_by_id, and can be
    tested in the same manner as that function too."""
    found_books = list(filter(lambda t: t["id"] == id, books))
    if len(found_books) == 0:
        # added a status code here just as a reminder that you can do it.
        return jsonify({}), 404
    current_book = found_books[0]

    if 'title' in request.json:
        current_book['title'] = request.json['title']
    if 'author' in request.json:
        current_book['author'] = request.json['author']
    if 'title' in request.json:
        current_book['price'] = request.json['price']

    return jsonify(current_book)


@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    """DELETEs a book using a given ID."""
    found_books = list(filter(lambda t: t["id"] == id, books))
    if len(found_books) == 0:
        # added a status code here just as a reminder that you can do it.
        return jsonify({}), 404
    books.remove(found_books[0])
    return jsonify({"done": True})


if __name__ == '__main__':
    app.run(debug=True)
