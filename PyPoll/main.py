# Modules
import os
import csv


# Store the filepath in a variable
path = 'resources/election_data.csv'
file = open(path, newline='')
reader = csv.reader(file)

# The first line is the header
header = next(reader) 

Total_Votes = 0
Candidates = []
Winner = 0
Winning_Candidate = ""
percentage = []
Vote_Count = []
percent = 0
Unique_Candidate_List = []

# Create Output file
analyzed_path = "Analysis/Polling_Analysis.txt"
Outfile = open(analyzed_path, 'w+')

# Caluclate the total number of votes

for row in reader:
    Total_Votes += 1

    # Determine the complete list of unique candidates
    # Add candidates to list

    Candidates.append(row[2])

# Begin writing to the output file and printing to terminal

Outfile.write("Election Results" + "\n")
Outfile.write("-------------------------" + "\n")
Outfile.write("Total Votes: " + str(Total_Votes) + "\n")
Outfile.write("-------------------------" + "\n")

print(
"Election Results" + "\n"
"-------------------------" + "\n"
"Total Votes: " + str(Total_Votes) + "\n"
"-------------------------" + "\n"
)
    
for row in Candidates: 
    if row not in Unique_Candidate_List:
        Unique_Candidate_List.append(row)

for name in Unique_Candidate_List:
    count = 0
    for row in Candidates:
        if name == row:
            count += 1
            percent = float(count) / float(Total_Votes) * 100
        if count > Winner:
            Winner = count
            Winning_Candidate = name
    
    i = Unique_Candidate_List.index(name)
    
# Put data to the lists
    percentage.append(percent)
    Vote_Count.append(count) 
    
# Write/print this part of the out file inside the loop to loop through the candidate info using the index
    Outfile.write(f"{Unique_Candidate_List[i]}: {percentage[i]:.3f}% ({Vote_Count[i]})\n")
    print(f"{Unique_Candidate_List[i]}: {percentage[i]:.3f}% ({Vote_Count[i]})\n")

# Write/print remaining portions of the output outside of the loop to avoid duplicating outputs
  
Outfile.write("-------------------------" + "\n")
Outfile.write("Winner: " + Winning_Candidate + "\n")
Outfile.write("-------------------------")

print(
"-------------------------" + "\n"
"Winner: " + Winning_Candidate + "\n"
"-------------------------"
)






    

