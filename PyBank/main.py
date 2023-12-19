#Import programs
import os
import csv

##Create variables
date = []
profits = []
profit_change = []

##Open CSV and assign name, skip header row, assign columns
## CHANGE TO RELATIVE PATH
with open('C:\\Users\\cdj3e\\vu_bootcamp\\Python\\Module_3_Challenge\\python_challenge\\PyBank\\resources\\budget_data.csv', "r") as financial_analysis:
    reader = csv.reader(financial_analysis)
    next(reader)
    for row in reader:
        date.append(row[0])
        profits.append(float(row[1]))

##Create loop to get profit changes over time and then calculate average
for i in range(1, len(profits)):
    profit_change.append(profits[i] - profits[i-1])
    average_change = sum(profit_change)/len(profit_change)

##Calculate minimum and maximum profit change
    max_change = max(profit_change)
    min_change = min(profit_change)

##Record minimum and maximum profit change dates
    max_date = str(date[profit_change.index(max(profit_change))])
    min_date = str(date[profit_change.index(min(profit_change))])

##Print results
print("Financial Analysis:")
print("---------------------------------")
print("Total Months:", str(len(date)))
print("Total: $", str(round(sum(profits))))
print("Average Change: $", round(average_change, 2))
print("Greatest Increase in Profits: ", max_date, "($", round(max_change) +1, ")")
print("Greatest Decrease in Profits: ", min_date, "($", round(min_change) +1, ")")