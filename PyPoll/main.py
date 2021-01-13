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
Unique_Candidate = set()
Winner = 0
Winning_Candidate = ""
percentage = []
Vote_Count = []
percent = 0
Unique_Candidate_List = ["O'Tooley", "Khan", "Correy", "Li"]

# Caluclate the total number of votes


for row in reader:
    Total_Votes += 1

    # Determine the complete list of unique candidates

    Unique_Candidate.add(row[2])

    # Add candidates to list

    Candidates.append(row[2])


for name in Unique_Candidate:
    count = 0
    for row in Candidates:
        if name == row:
            count += 1
            percent = float(count) / float(Total_Votes) * 100
        if count > Winner:
            Winner = count
            Winning_Candidate = name

    # Put data to the lists
    percentage.append(percent)
    Vote_Count.append(count) 

    i = Unique_Candidate_List.index(name)


analyzed_path = "Analysis/Polling_Analysis.txt"
Outfile = open(analyzed_path, 'w+')

Outfile.write("Election Results" + "\n")
Outfile.write("-------------------------" + "\n")
Outfile.write("Total Votes: " + str(Total_Votes) + "\n")
Outfile.write("-------------------------" + "\n")
Outfile.write({Unique_Candidate_List[i]} + ":" + str(percentage[i]) + "%" + str(Vote_Count[i]) + "\n")
Outfile.write("-------------------------" + "\n")
Outfile.write("Winner: " + Winning_Candidate + "\n")
Outfile.write("-------------------------")


    

