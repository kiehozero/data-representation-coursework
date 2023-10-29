import json
import requests

# Variables for the parts of the CSO's API requests that do not change
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
apiFormat = "/JSON-stat/2.0/en"

def getAll(dataset):
    endpoint = url + dataset + apiFormat
    response = requests.get(endpoint)
    return response.json()

if __name__ == "__main__":
    with open("cso.json","wt") as fp:
        print(json.dumps(getAll("FIQ02")), file=fp)