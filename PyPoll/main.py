# $ /usr/bin/python3 ./PyPoll/main.py

import os
import csv

# define path to CSV file
file_path = 'PyPoll/Resources/election_data.csv'

# initialize variables
total_votes = 0
candidates = {}
candidates_list = []

# open and read csv file
with open(file_path, "r") as csvfile:
    csvreader = csv.reader(csvfile)

    # read the header
    header = next(csvreader)

    # loop through each row in the csv
    for row in csvreader:
        total_votes += 1
        candidate = row[2]

        if candidate not in candidates:
            candidates[candidate] = 0
            candidates_list.append(candidate)

        candidates[candidate] += 1

# calculate the percentage of votes each candidate won
candidate_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidates.items()}

# determine winner of election
winner = max(candidates, key=candidates.get)

# generate output string
def generate_output():
    output = (
        "Election Results\n"
        "-------------------------\n"
        f"Total Votes: {total_votes}\n"
        "-------------------------\n"
    )
    for candidate in candidates_list:
        output += f"{candidate}: {candidate_percentages[candidate]:.3f}% ({candidates[candidate]})\n"
    output += (
        "-------------------------\n"
        f"Winner: {winner}\n"
        "-------------------------\n"
    )
    return output

# Print the analysis to the console
print(generate_output())

# Write the analysis to a text file
output_file_path = os.path.join("PyPoll", "analysis")
os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
output_file_path = "PyPoll/analysis.txt"
with open(output_file_path, "w") as txtfile:
    txtfile.write(generate_output())