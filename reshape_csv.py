# Nov 27 2020
# Big Data project
# reshape data from ipums output to 
# [[year, serial, month, ..., diffany, faminc2, marst2, nchild2, empstat2, labforce2, wkstat2], ...]

import numpy as np 
from collections import defaultdict
import csv 

filename = "cps_00003.csv"

data = [] 
  
# opening the CSV file 
with open(filename, mode ='r') as file:     
       # reading the CSV file 
       csvFile = csv.reader(file) 
       # displaying the contents of the CSV file 
       for line in csvFile: 
            data.append(line) 


newVars = data[0] + ['FAMINC2', 'MARST2', 'NCHILD2', 'EMPSTAT2', 'LABFORCE2', 'WKSTAT2', 'SCHLCOLL2']
newVarLocs = [8, 18, 21, 27, 28, 34]
data2 = []
data2.append(newVars)

# make dict of person : all their observations 
personDict = defaultdict(list) # keys are CPSIDPs
for i in range(1, len(data)):
    perID = data[i][13]
    row = data[i] 
    personDict[perID].append(row)  
    
# loop through dict 
for key in personDict.keys(): 
    if len(personDict[key])==2: # if the person has 2 observations 
        if personDict[key][0][0]=='2018':
            row = personDict[key][0]
            for i in newVarLocs: # loop through the new variables 
                row.append(personDict[key][1][i]) # and add them to the end of the row 
            data2.append(row) # add the new observation to data2 
        elif personDict[key][1][0]=='2018':
            row = personDict[key][0]
            for i in newVarLocs: 
                row.append(personDict[key][0][i]) 
            data2.append(row)
        else:
            print("we have a problem") 

# output to csv 
file2 = "cps3_reshape.csv"
fields = data2[0] 
rows = data2[1:] 
with open(file2, 'w') as csvfile: 
    # creating a csv writer object 
    csvWriter = csv.writer(csvfile) 
    # writing the fields 
    csvWriter.writerow(fields) 
    # writing the data rows 
    csvWriter.writerows(rows)