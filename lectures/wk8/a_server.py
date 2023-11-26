"""
A basic Flask setup. Run this file as a normal Python file, then use the IP
address 127.0.0.1 in the browser to display. Alternatively, use the command
FLASK_APP=a_server (or whatever the filename is), then the command 'flask run'.
"""
from flask import Flask, url_for, redirect

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


if __name__ == '__main__':
    app.run(debug=True)
