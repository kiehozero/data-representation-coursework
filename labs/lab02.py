import csv
import requests as req
import xml.dom.minidom as x

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = req.get(url)
doc = x.parseString(page.content)

# print(doc.toprettyxml())

# writes data to a file. If the file does not exist, it is created
with open("currenttrains.xml","w") as xml_file:
    doc.writexml(xml_file)

trainList = doc.getElementsByTagName("objTrainPositions")

for train in trainList:
    codeNode = train.getElementsByTagName("TrainCode").item(0)
    latNode = train.getElementsByTagName("TrainLatitude").item(0)
    trainCode = codeNode.firstChild.nodeValue.strip()
    trainLat = latNode.firstChild.nodeValue.strip()
    print(f'Train Code: {trainCode}, Lat: {trainLat}')

