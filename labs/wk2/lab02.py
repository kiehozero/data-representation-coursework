import csv
import requests as req
import xml.dom.minidom as x

# Connect to a URL and endpoint
url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = req.get(url)
doc = x.parseString(page.content)

# A list of tags contained in the XML data, to be used later
tagArr = ['TrainCode', 'TrainStatus', 'TrainDate', 'Direction',
          'TrainLatitude', 'TrainLongitude', 'PublicMessage']

# print(doc.toprettyxml())

# Writes data to a file. If the file does not exist, it is created
with open("currenttrains.xml", "w") as xml_file:
    doc.writexml(xml_file)

trainList = doc.getElementsByTagName("objTrainPositions")

# Loop through the trains and return the code and current latitude
for train in trainList:
    codeNode = train.getElementsByTagName("TrainCode").item(0)
    latNode = train.getElementsByTagName("TrainLatitude").item(0)
    trainCode = codeNode.firstChild.nodeValue.strip()
    trainLat = latNode.firstChild.nodeValue.strip()

# Combine the previous with and for loops to create a CSV
with open('currenttrains.csv', mode='w', newline='') as train_csv:
    train_writer = csv.writer(train_csv, delimiter='\t', quotechar='"',
                              quoting=csv.QUOTE_MINIMAL)
    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for node in objTrainPositionsNodes:
        dataList = []
        for tag in tagArr:
            trainNode = node.getElementsByTagName(tag).item(0)
            tagData = trainNode.firstChild.nodeValue.strip()
            dataList.append(tagData)
        train_writer.writerow(dataList)

# Read the CSV file and print the contents to the console
with open('currenttrains.csv', newline='') as train_csv:
    train_reader = csv.reader(train_csv, delimiter='\t', quotechar='"')
    for row in train_reader:
        print(', '.join(row))
