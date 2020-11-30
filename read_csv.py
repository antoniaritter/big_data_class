# Nov 20 
# Big data project 
# Exploring reading csv files from ipums 


import csv 

filename = "cps_00001.csv"

data = [] 
  
# opening the CSV file 
with open(filename, mode ='r') as file:     
         
       # reading the CSV file 
       csvFile = csv.DictReader(file) 
  
       # displaying the contents of the CSV file 
       for line in csvFile: 
            data.append(line) 

print(data[0]) 
