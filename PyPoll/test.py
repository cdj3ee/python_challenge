##Import programs
import os
import csv
from collections import defaultdict

##Assign variables
ballot_id = []
county = []
candidate = []
all_candidates = []

##Open CSV and assign name, skip header row, assign columns
with open('C:\\Users\\cdj3e\\vu_bootcamp\\Python\\Module_3_Challenge\\python_challenge\\PyPoll\\resources\\election_data.csv', "r") as election_analysis:
    reader = csv.reader(election_analysis)
    next(reader)
    for row in reader:
        ballot_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

##List all unique candidates
all_candidates = list(set(candidate))

print("Election Results")
print("------------------------")
print("Total Votes: ", str(len(ballot_id)))
print("------------------------")
print(all_candidates[0] +": ")
print(all_candidates[1] +": ")
print(all_candidates[2] +": ")
print("------------------------")
print("Winner: ")

print(all_candidates[1])