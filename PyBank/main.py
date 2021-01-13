# Modules
import os
import csv
from typing import Text

# Store the filepath in a variable
path = 'resources/budget_data.csv'
file = open(path, newline='')
reader = csv.reader(file)

header = next(reader) # The first line is the header

data = []
Date = []

for row in reader:
    # row = [Date, Profit/Losses]
    date = str([0])
    Profit_Losses = int(row[1])

    data.append([date, Profit_Losses])
    Date.append(row[0])

# Compute and store data
# Determine the total number of months included in the dataset
Total_Months = 0

for row in data:
    Total_Months += 1

# Determine Total the net total of profits and lossess over the enitre period

Total_Profits = sum(row[1] for row in data)

# Determine the the Average Change
# Store profit and losses column into a list
Profit_Losses_List = []
for row in data:
    
    Profit_Losses_List.append(row[1])

# Create a list for the change in profit/lossess between each month

Change = []
for i in range(len((Profit_Losses_List))-1):
    Change.append((Profit_Losses_List)[i+1] - (Profit_Losses_List)[i])

# Create function to calculate the average of all the values in our change list

def Average(list):
    return sum(list) / len(list)

Average_Change = round(Average(Change),2)

# Calculate the greatest increase in profits

Greatest_Increase_In_Profits = max(Change)

Increase_Index = Change.index(max(Change)) + 1


# Calculate the greatest decrease in profits

Greatest_Decrease_In_Profits = min(Change)

Decrease_Index = Change.index(min(Change)) + 1

# Determine what month produced the min/max profit changes


analyzed_path = "Analysis/Financial_Analysis.txt"
Outfile = open(analyzed_path, 'w+')

Outfile.write("Financial Analysis" + "\n")
Outfile.write("----------------------------" + "\n")
Outfile.write("Total Months: " + str(Total_Months) + "\n")
Outfile.write("Total: $" + str(Total_Profits) + "\n")
Outfile.write("Average Change: $" + str(Average_Change) + "\n")
Outfile.write("Greatest Increase in Profits: " + str(Date[Increase_Index]) + " ($" + str(Greatest_Increase_In_Profits) + ")" + "\n")
Outfile.write("Greatest Decrease in Profits: " +  str(Date[Decrease_Index]) + " ($" + str(Greatest_Decrease_In_Profits) + ")" + "\n")


print(
    "Financial Analysis" + "\n"
    "----------------------------" + "\n"
    "Total Months: " + str(Total_Months) + "\n"
    "Total: $" + str(Total_Profits) + "\n"
    "Average Change: $" + str(Average_Change) + "\n"
    "Greatest Increase in Profits: " + str(Date[Increase_Index]) + " ($" + str(Greatest_Increase_In_Profits) + ")" + "\n"
    "Greatest Decrease in Profits: " +  str(Date[Decrease_Index]) + " ($" + str(Greatest_Decrease_In_Profits) + ")" + "\n"
    )
