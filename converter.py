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
#creating a new csv file from the table names 
def createCsvFile(fileName):
    return open(fileName+'.csv','w')


#main open
sqlFile = open('demo.sql', 'r')
#sqlFile = open('/c/Users/leonm/Desktop/python/Hw/tar2/SQL-to-CSV-converter/demo.sql','r')
#csvFile = open('/c/Users/leonm/Desktop/python/Hw/tar2/SQL-to-CSV-converter/csvfile.txt', 'w')
content = sqlFile.read()
csvFile = open('csvfile.txt', 'w')
sqlFile.close()
tables = content.split("CREATE TABLE") #spliting the content of the file by the tables with or without their values

filtered2 = list(filter(insertIntoExists, tables))[1].replace(" ", "").split('\n') #removes unnecesry tables without conetnt 
titles=getTitles(filtered2) #the name is located in the first tile and the table titles in the rest
csvForTest=createCsvFile(titles[0])
printTitles(csvForTest,titles[1:])
#main close
csvFile.close()