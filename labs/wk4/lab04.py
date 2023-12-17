# Implement all the API calls as functions

import requests

url = "http://andrewbeatty1.pythonanywhere.com/books"


def getAllBooks():
    response = requests.get(url)
    # in production code you would want to check the status code each time
    return response.json()


def getBook(id):
    geturl = url + "/" + str(id)
    response = requests.get(geturl)
    return response.json()


def createBook(book):
    response = requests.post(url, json=book)
    return response.json()


def updateBook(id, bookdiff):
    updateurl = url + "/" + str(id)
    response = requests.put(updateurl, json=bookdiff)
    return response.json()


def deleteBook(id):
    deleteurl = url + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()


if __name__ == "__main__":
    book = {
        'Author': "Michel Foucault",
        'Title': "Discipline and Punish",
        'Price': 100
    }
    bookdiff = {
        'Price': 85
    }
    print(getAllBooks())
    # print(getBook(342))
    # print(createBook(book))
    print(updateBook(345, bookdiff))
    # print(deleteBook(324))
