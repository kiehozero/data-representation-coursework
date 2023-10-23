# Exploring a dataset via the APIs at data.gov.ie

import json
import requests
import urllib.parse

url = "https://api.valoff.ie/api/Property/GetProperties"

param_dict = {
    "Download": "false",
    "Format": "json",
    "CategorySelected": "OFFICE",
    "LocalAuthority": "WICKLOW COUNTY COUNCIL",
    "Fields":"LocalAuthority,Category,Level,AreaPerFloor,NavTotal,CarPark,PropertyNumber,IG,Use,FloorUse,Address,PublicationDate"

}

def getAll():
    parameters = urllib.parse.urlencode(param_dict)
    print(parameters)
    full_url = url + "?" + parameters

    response = requests.get(full_url)

    return response.json()

if __name__ == "__main__":
    with open("val_office.json", "wt") as fp:
        print(json.dumps(getAll()),file=fp)