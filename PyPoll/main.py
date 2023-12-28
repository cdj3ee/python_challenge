## Import Programs
import os
import csv

# Assign variables
ballot_id = []
all_candidates = []

# Open CSV and assign name, skip header row, assign columns
with open('C:\\Users\\cdj3e\\vu_bootcamp\\Python\\Module_3_Challenge\\python_challenge\\PyPoll\\resources\\election_data.csv', "r") as election_analysis:
    reader = csv.reader(election_analysis)
    next(reader)
    for row in reader:
        ballot_id.append(row[0])
        all_candidates.append(row[2])

# List all unique candidates
candidates_set = set(all_candidates)
candidates_dict = {candidate: {'count': all_candidates.count(candidate), 'percent': 0.0} for candidate in candidates_set}

# Find total number of votes
total_votes = len(ballot_id)

# Calculate percentages for candidates
for candidate, data in candidates_dict.items():
    data['percent'] = round((data['count'] / total_votes) * 100, 3)

# Identify winner
winner = max(candidates_dict, key=lambda x: candidates_dict[x]['count'])

# Print results
print("Election Results")
print("-------------------------")
print("Total Votes: ", total_votes)
print("-------------------------")
for candidate, data in candidates_dict.items():
    print(f"{candidate}: {data['percent']}% ({data['count']})")
print("-------------------------")
print("Winner: ", winner)
print("-------------------------")

# Write results to a csv file
output_file = 'election_results.csv'
with open(output_file, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Candidate', 'Percentage', 'Votes'])   
    for candidate, data in candidates_dict.items():
        csvwriter.writerow([candidate, f"{data['percent']}%", data['count']])   
    csvwriter.writerow(['Total Votes', total_votes])
    csvwriter.writerow(['Winner', winner])
