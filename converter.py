def insertIntoExists(section):
	return section.find("INSERT INTO") != -1

def getTitles(section):
	i = 0
	temp = []
	while section[i][0] == '`':
		#get section of row in between ` ` to get titles
		temp.append(section[i][1:str(section[i][1:]).find('`')+1])
		i += 1
	return temp

def printTitles(outputFile, lst):
	for i in lst:
		#print in csv
		outputFile.write("'{}',".format(i))
	outputFile.write('\n\n')

def printData(section):
	for line in section:
		if line.startswith("INSERT INTO"):
			substr = line
			while len(substr) != 1:
				csvFile.write(substr[substr.find('(')+1:substr.find(')')])

sqlFile = open('demo.sql', 'r')
csvFile = open('csvfile.txt', 'w')
content = sqlFile.read()
sqlFile.close()

sqlWords = content.split("CREATE TABLE")
counter = 0

filtered = list(filter(insertIntoExists, sqlWords))[1].split('\n')
filtered2 = list(filter(insertIntoExists, sqlWords))[1].replace(" ", "").split('\n')
printTitles(csvFile, getTitles(filtered2))
