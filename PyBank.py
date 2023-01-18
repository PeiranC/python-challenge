import os
import csv
pybank_csv = os.path.join("Resources","budget_data.csv")

profits=[]
date = []
monthly_change = []

with open (pybank_csv, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

    for row in csvreader:
        date.append(row[0])

        profits.append(int(row[1]))

for x, row in enumerate (profits):
    if x>0:
        monthly_change.append(profits[x]-profits[x-1])

os.mkdir("Analysis")
result = os.path.join ("Analysis", "result_PyBank.txt")

with open (result, "w") as f:
    
    f.write("Financial Analysis \n")    
    f.write("------------------\n")
    f.write("Total Months: " + str(len(date)) + "\n")
    f.write("Total: " + "$" + str(sum(profits)) + "\n")
    f.write("Average Change: " + "$" + str(round(sum(monthly_change)/len(monthly_change), 2)) + '\n')

print("Financial Analysis")
print("------------------")
print(f"Total Months: {len(date)}")
print(f"Total : ${sum(profits)}")


date.pop(0)
print(f"Average Change: ${round(sum(monthly_change)/len(monthly_change), 2)}")


for i, row in enumerate(monthly_change):
    
    if monthly_change [i]>=max(monthly_change):
        with open(result, 'a') as f:
            f.write("Greatest Increase in Profits:" + str(date[i]) + "($"+ str(max(monthly_change))+ " \n")
        print(f"Greatest Increase in Profits: {date[i]} (${max(monthly_change)})")   
        
   
    if monthly_change [i]<=min(monthly_change):
        with open(result, 'a') as f:
            f.write("Greatest Decrease in Profits:" + str(date[i]) + "($" + str(min(monthly_change))+ " \n")  
        print(f"Greatest Decrease in Profits: {date[i]} (${min(monthly_change)})")












