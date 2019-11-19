# import csv
# with open('eggs.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in spamreader:
#         print(', '.join(row))
#------------------------------------

# import csv
# targetList=[1,23,4]
# with open('newFile.csv', 'w',encoding='utf-8',newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(targetList)
# -----------------

import csv

# Read csv file
csvFile = r'C:\code\idk\eggs.csv'
f=open(csvFile,'rt')
myReader = csv.reader(f)

# Write new csv
targetList=[1,2,3,4]

with open( 'oldFile.csv', 'w', encoding='utf-8', newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(targetList)

# Write in Existing csv
with open ( 'eggs.csv', 'a') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(targetList)
