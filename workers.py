import csv
workersAndPercent = {}
with open('occupations.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        workersAndPercent[row[0]] = row[1]
workersAndPercent.pop('Job Class','Percentage')
for x in workersAndPercent.values():
  print(x)
