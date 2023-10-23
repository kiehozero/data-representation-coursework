from val_office import getAll

data = getAll()
totalArea = 0

for entry in data:
    val_report = entry["ValuationReport"]
    for val in val_report:
        if val["FloorUse"] == "HAIR SALON":
            totalArea += val["Area"]

print(totalArea)
