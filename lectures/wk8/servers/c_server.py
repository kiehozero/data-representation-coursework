from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello Mammzdfsdfy"


# providing data from a URL query string (as arguments)
@app.route('/datainquery', methods=['GET'])
def inquery():
    queryargs = {
        "firstname": request.args["firstname"],
        "age": request.args["age"]
    }
    print(queryargs)
    return jsonify(queryargs)


# providing data using a JSON file
@app.route('/dataasjson', methods=['POST'])
def asjson():
    book = {
        "title": request.json["title"],
        "author": request.json["author"],
        "price": request.json["price"]
    }
    # you'd add some pymysql functions here to add the data to the DB
    print(book)
    return jsonify(book)


if __name__ == "__main__":
    app.run(debug=True)
