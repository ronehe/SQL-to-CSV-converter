#creators -----Ronen heifetz 316481423 , Markovich Leon 318375060-----
#please make sure to create a folder named "csvFiles" in the same directory before running !!!!!!!!!!!!!

#finding full tables for which be counted in the excel
def insertIntoExists(section):
    return section.find("INSERT INTO") != -1

#getting the titles from the usful tables
def getTitles(section):
    i = 0 
    temp = []
    while section[i][0] == '`':
        #get section of row in between ` ` to get titles
        temp.append(section[i][1:str(section[i][1:]).find('`')+1] + ',')
        i += 1
    return temp

#returns the tables data
def getData(section):
	output =[]
	for line in section:
		if line.startswith("INSERTINTO"):
			output=line.split('(')
			output=output[1:]
			output=[x[:-2] for x in output]    
	return output
#creating a new csv file from the table names 
def createCsvFile(fileName):
    return open('csvFiles\\' +fileName+'.csv','w')

#main open
sqlFile = open('demo.sql', 'r')
csvFile = open('csvfile.txt', 'w')
content = sqlFile.read()
sqlFile.close() #closing the sql file not needed after making it a string
tables = content.split("CREATE TABLE") #spliting the content of the file by the tables with or without their values

filtered2 = list(filter(insertIntoExists, tables))
for i in filtered2:
    tablesWithoutSpaces=i.replace(" ", "").split('\n') #removes unnecesry tables without conetnt 
    titles=getTitles(tablesWithoutSpaces) #the name is located in the first tile and the table titles in the rest
    table = titles[1:] #the name of the table is in tile 0 and the rest of it is its titles
    outputFile=createCsvFile(str(titles[0])[:-1])
    outputFile.write(','.join(([x[:-1] for x in table]))+'\n\n'+('\n\n'.join(getData(tablesWithoutSpaces)))) # sepeating the list of titles without ' 
    outputFile.close() #closing each opened file

#main close
