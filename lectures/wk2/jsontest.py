import json
import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)

# check status HTTP code and returned data
# print(response)
# print(response.json())

prices = response.json()

# pushes retrieved data into a JSON file. If it does not exist, it is created.
# HINT: If you press Alt Shift F inside any file, it will correctly indent the file to make it more readable
with open("simple.json", "w") as f:
    json.dump(prices, f)

euro = prices["bpi"]["EUR"]
rate = euro["rate"]

print(rate)