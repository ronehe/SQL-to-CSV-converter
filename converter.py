import os
import sys
import csv

def insertIntoExists(section):
    return section.find("INSERT INTO") != -1

def getTitles(section):
    i = 0 
    temp = []
    while section[i][0] == '`':
        #get section of row in between ` ` to get titles
        temp.append(section[i][1:str(section[i][1:]).find('`')+1] + ',')
        i += 1
    
    return temp

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
    folder='csvFiles\\'
    return open(folder +fileName+'.csv','w')

#main open
sqlFile = open('demo.sql', 'r')
#sqlFile = open('/c/Users/leonm/Desktop/python/Hw/tar2/SQL-to-CSV-converter/demo.sql','r')
#csvFile = open('/c/Users/leonm/Desktop/python/Hw/tar2/SQL-to-CSV-converter/csvfile.txt', 'w')
content = sqlFile.read()
csvFile = open('csvfile.txt', 'w')
sqlFile.close()
tables = content.split("CREATE TABLE") #spliting the content of the file by the tables with or without their values

filtered2 = list(filter(insertIntoExists, tables))
for i in filtered2:
    i.replace(" ", "").split('\n') #removes unnecesry tables without conetnt 
    titles=getTitles(i) #the name is located in the first tile and the table titles in the rest
    table = titles[1:]
    outputFile=createCsvFile(str(titles[0])[:-1])
    outputFile.write(','.join(([x[:-1] for x in table]))+'\n\n'+('\n\n'.join(getData(i)))) # sepeating the list of titles without ' 
    outputFile.close()
#main close
