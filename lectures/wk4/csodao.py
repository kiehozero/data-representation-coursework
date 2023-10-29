import json
import requests

# Variables for the parts of the CSO's API requests that do not change
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
apiFormat = "/JSON-stat/2.0/en"

# A function that simply returns the dataset required, most of the other functions will use this before further customising it
def getAllAsVar(dataset):
    endpoint = url + dataset + apiFormat
    response = requests.get(endpoint)
    return response.json()

# A function that saves a returned dataset as a JSON file. If the file does not exist, it is created
def getAllAsFile(dataset):
    with open("csodao.json","wt") as fp:
        print(json.dumps(getAllAsVar(dataset)), file=fp)

def getFormattedAsVar(dataset):
    data = getAllAsVar(dataset)
    # creating a variable for each of the top-level dictionary items
    ids = data["id"]
    values = data["value"]
    dims = data["dimension"]
    size = data["size"]

    val_count = 0
    result = {}

    for dim0 in range(0,size[0]):
        currentId = ids[0]
        index = dims[currentId]["category"]["index"][dim0]
        label0 = dims[currentId]["category"]["label"][index]
        result[label0] = {}

        for dim1 in range(0,size[1]):
            currentId = ids[1]
            index = dims[currentId]["category"]["index"][dim1]
            label1 = dims[currentId]["category"]["label"][index]
            # print(f'\t{currentId}\t{index}\t{label}')
            result[label0][label1] = {}

            for dim2 in range(0,size[2]):
                currentId = ids[2]
                index = dims[currentId]["category"]["index"][dim2]
                label2 = dims[currentId]["category"]["label"][index]
                # print(f'\t\t{currentId}\t{index}\t{label}')
                result[label0][label1][label2] = {}

                for dim3 in range(0,size[3]):
                    currentId = ids[3]
                    index = dims[currentId]["category"]["index"][dim3]
                    label3 = dims[currentId]["category"]["label"][index]
                    # print(f'\t\t\t{currentId}\t{index}\t{label},{values[val_count]}')
                    result[label0][label1][label2][label3] = values[val_count]
                    val_count += 1
    
    return result

def getFormattedAsFile(dataset):
    with open("csodao_formatted.json","wt") as fp:
        print(json.dumps(getFormattedAsVar(dataset)), file=fp)

# This section can be used to modify the exact dataset required
if __name__ == "__main__":
    ds = "FP001"
    getAllAsVar("FP001")
    getFormattedAsVar("FP001")
    getFormattedAsFile("FP001")
