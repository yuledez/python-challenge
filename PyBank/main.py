# Modules
import os
import csv
#variables
total_months =  0
total_amount = 0

#set path for file
script_directory= os.path.dirname(os.path.abspath (__file__))


csvpath = r"Resources\budget_data.csv"
path2 = os.path.join(script_directory,csvpath)

print ("aqui:   " + path2)
#open csv
with open(path2, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #loop through budget data csv
    for row in csvreader:
        if row[0] != "Date":
            total_months = total_months + 1
            total_amount = total_amount +  int(row[1])


print ("Finacial Analysis")
print ("---------------------------")
print ("Total Months: " + str(total_months))
print ("Total: " + str(total_amount))
print ("Average Change: ")
print ("Greatest Increase in Profits: ")
print ("Greatest Decrease in Profits: ")


