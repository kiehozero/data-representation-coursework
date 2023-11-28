"""
A basic Flask setup. Run this file as a normal Python file, then use the IP
address 127.0.0.1 in the browser to display. Alternatively, use the command
FLASK_APP=a_server (or whatever the filename is), then the command 'flask run'.
"""
from flask import Flask, url_for, redirect, request, jsonify

app = Flask(__name__, static_url_path='', static_folder='static')


@app.route('/')
def index():
    """Function for default URL, returns link from another function."""
    return "<a href=" + url_for('get_user') + ">Get Users</a>"


@app.route('/user', methods=['GET'])
def get_user():
    """Introducing paths and methods, note that isn't tied to a particular
    static file, so typing user.html in the address would not work. You can
    even testmethods in Postman by using the same IP plus the route name."""
    return "Hi user "


@app.route('/user', methods={'POST'})
def post_user():
    """Same as above but with a different method."""
    return "Post user"


@app.route('/user/<int:userid>', methods=['GET'])
def id_user(userid):
    """Passing values to the route."""
    return "Hi user " + str(userid)


@app.route('/invalid', methods=['GET'])
def invalid():
    """Using redirections for basic error handling."""
    return redirect(url_for('index'))


@app.route('/datainquery', methods=['GET'])
def in_query():
    """Using request to return data from query arguments. In this case the URL
    would be http://127.0.0.1:5000/datainquery?first_name=Stuart&age=36"""
    query_args = {
        "first_name": request.args["first_name"],
        "age": request.args["age"]
    }
    return jsonify(query_args)


@app.route('/data_json', methods=['GET'])
def in_json():
    """Using JSON data."""
    book = {
        "title": request.json["title"],
        "author": request.json["author"],
        "price": request.json["price"]
    }
    print(book)
    # this function works only in Postman right now, to see the corrected
    # version, look at the create_book function in the rest_server.py file
    # in the REST-example folder.
    return jsonify(book)


if __name__ == '__main__':
    app.run(debug=True)
