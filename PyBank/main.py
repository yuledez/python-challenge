# import libraries
import os
import csv
#variables
total_months =  0
total_amount = 0
prev_profit_loss = None
diff = []

#set path for input file
script_directory= os.path.dirname(os.path.abspath (__file__))
csvpath = r"Resources\budget_data.csv"
path2 = os.path.join(script_directory,csvpath)

#set path for output file
txtpath = r"analysis\results.txt"
out_path = os.path.join(script_directory,txtpath)

#open csv
with open(path2, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile)

    next(csvreader) 
    #loop through budget data csv
    for row in csvreader:
       total_months += 1
       total_amount += int(row[1])
       date = row[0]
       profit_loss = int(row[1])

       if prev_profit_loss is not None:
          change = profit_loss - prev_profit_loss
          diff.append((date, change))

       prev_profit_loss = profit_loss

gr_increase = max(diff, key=lambda x: x[1])
gr_decrease = min(diff, key=lambda x: x[1])


temp_sum = 0
for x in diff:
   temp_sum += x[1]
average_diff = temp_sum / len(diff)

#average_diff = sum(x[1] for x in diff) / len(diff) #simplified way to get average from tuple

#Print results
#
output = (
   "\n"
   "Finacial Analysis\n"
   "---------------------------\n"
   f"Total Months: {total_months}\n"
   f"Total: ${total_amount}\n"
   f"Average Change: ${average_diff:.2f}\n"
   f"Greatest Increase in Profits: {gr_increase[0]} (${gr_increase[1]})\n"
   f"Greatest Decrease in Profits: {gr_decrease[0]} (${gr_decrease[1]})\n"
   )

print(output)

with open(out_path, mode='w') as file:
    file.write(output)


