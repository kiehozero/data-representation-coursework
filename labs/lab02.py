import csv
import requests as req
import xml.dom.minidom as x

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = req.get(url)
doc = x.parseString(page.content)

# writes data to a file. If the file does not exist, it is created
with open("currenttrains.xml","w") as xml_file:
    doc.writexml(xml_file)

parsed = x.parse(xml_file)

trainList = doc.getElementsByTagName("objTrainPositions")