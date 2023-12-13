##Import programs
import os
import csv

##Assign variables
ballot_id = []
all_candidates = []
percentages = []
counts = []

##Open CSV and assign name, skip header row, assign columns
with open('C:\\Users\\cdj3e\\vu_bootcamp\\Python\\Module_3_Challenge\\python_challenge\\PyPoll\\resources\\election_data.csv', "r") as election_analysis:
    reader = csv.reader(election_analysis)
    next(reader)
    for row in reader:
        ballot_id.append(row[0])
        all_candidates.append(row[2])

##List all unique candidates
candidate = list(set(all_candidates))

##Find total number of votes
total_votes = len(ballot_id)

##Calculate counts and percentages for candidates
for candidate in all_candidates:
    count = all_candidates.count(candidate)
    percent = round((count / total_votes) * 100, 3)
    counts.append(count)
    percentages.append(percent)

##Create for loop and float to print corresponding candidate, vote percentage, and vote count
for i in range(len(candidate)):
    print(f"{candidate[i]}: {percentages[i]}% ({counts[i]})")

##Identify winner and assign variable
winner_index = counts.index(max(counts))
winner = candidate(winner_index)

##print results
print("Election Results")
print("------------------------")
print("Total Votes: ", total_votes)
print("------------------------")
for i in range(len(candidate)):
    print(f"{candidate[i]}: {percentages[i]}% ({counts[i]})")
print("------------------------")
print("Winner: ", winner) 
print("------------------------")
