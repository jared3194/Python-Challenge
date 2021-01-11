# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
# You will give a set of financial data called budget_data.csv. 
# The dataset is composed of two columns: Date and Profit/Losses. 
# (Thankfully, your company has rather lax standards for accounting so the records are simple.)

# Your task is to create a Python script that analyzes the records to calculate each of the following:
# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period

# As an example, your analysis should look similar to the one below:

# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# Modules
import os
import csv
from datetime import datetime
from typing import Text

# Store the filepath in a variable
path = 'resources/budget_data.csv'
file = open(path, newline='')
reader = csv.reader(file)

header = next(reader) # The first line is the header

data = []
for row in reader:
    # row = [Date, Profit/Losses]
    date = datetime.strptime(row[0], '%b-%Y')
    Profit_Losses = int( row[1])

    data.append([date, Profit_Losses])

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
print(Greatest_Increase_In_Profits)

# Calculate the greatest decrease in profits

Greatest_Decrease_In_Profits = min(Change)

# Determine what month produced the min/max profit changes


# Greatest_Decrease_Month = Change.index((Greatest_Decrease_In_Profits) + 1)
# print(Greatest_Decrease_Month)

# print(Greatest_Decrease_Month)

analyzed_path = "Analysis/Financial_Analysis.txt"
Outfile = open(analyzed_path, 'w+')

Outfile.write("Financial Analysis" + "\n")
Outfile.write("----------------------------" + "\n")
Outfile.write("Total Months: " + str(Total_Months) + "\n")
Outfile.write("Total: $" + str(Total_Profits) + "\n")
Outfile.write("Average Change: $" + str(Average_Change) + "\n")
Outfile.write("Greatest Increase in Profits: $" + str(Greatest_Increase_In_Profits) + "\n")
Outfile.write("Greatest Decrease in Profits: $" + str(Greatest_Decrease_In_Profits) + "\n")



