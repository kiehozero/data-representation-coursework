import json
import requests

# Variables for the parts of the CSO's API requests that do not change.
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
apiFormat = "/JSON-stat/2.0/en"

# A function to request and return data using the variables above and a given dataset ID.
def getAll(dataset):
    endpoint = url + dataset + apiFormat
    response = requests.get(endpoint)
    return response.json()

# Passes the dataset's ID to the main function, then creates a JSON file with the returned data.
if __name__ == "__main__":
    with open("cso.json","wt") as fp:
        print(json.dumps(getAll("FIQ02")), file=fp)