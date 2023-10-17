from xml.dom.minidom import parse

filename = "employees.xml"

doc = parse(filename)

empNodeList = doc.getElementsByTagName("Employee")

print(len(empNodeList))
print("------")
print(empNodeList)
print("------")

for empNode in empNodeList:
    firstNameNode = empNode.getElementsByTagName("FirstName").item(0)
    firstName = firstNameNode.firstChild.nodeValue.strip()
    print(firstName)

