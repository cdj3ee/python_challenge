##Import programs
import os
import csv

##Assign variables
ballot_id = []
all_candidates = {}
all_candidates_list = []
percentages = []
counts = []

##Open CSV and assign name, skip header row, assign columns
with open('C:\\Users\\cdj3e\\vu_bootcamp\\Python\\Module_3_Challenge\\python_challenge\\PyPoll\\resources\\election_data.csv', "r") as election_analysis:
##with open(os.path.join("Resources", "election_data.csv")) as election_analysis:
    reader = csv.reader(election_analysis)
    next(reader)
    for row in reader:
        ballot_id.append(row[0])
        candidate = (row[2])
        if candidate not in all_candidates_list:
            all_candidates_list.append(candidate)
            all_candidates[candidate] = 0
        all_candidates[candidate] += 1


##List all unique candidates
candidate = list(set(all_candidates))

print(all_candidates)

##Find total number of votes
total_votes = len(ballot_id)

##Calculate counts and percentages for candidates
## GO THROUGH CANDIDATES NAMES FOR VOTE COUNT (all_candidates_list, count = all_candidates[candidate])

##candidates_list = all_candidates[candidate]
for candidate in all_candidates_list:
    count = all_candidates_list.count(candidate)
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
