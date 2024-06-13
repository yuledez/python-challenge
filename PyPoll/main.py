import os
import csv
total_votes = 0
votes_per_candidate = {}


# Path to collect data from the Resources folder
script_directory= os.path.dirname(os.path.abspath (__file__))
csvpath = r"Resources\election_data.csv"
election_csv = os.path.join(script_directory,csvpath)


#open csv, split data with commas
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    #loop
    for row in csvreader:
        #total number of votes
        total_votes += 1
        candidate_name = row[2]
       
        if candidate_name in votes_per_candidate:
            votes_per_candidate[candidate_name] += 1
        else:
            votes_per_candidate[candidate_name] = 1
        

    # get canditates and percentages
    vote_percentage = {candidate: (votes / total_votes) * 100 for candidate, votes in votes_per_candidate.items()}

    #winner
    election_winner = max(votes_per_candidate, key=votes_per_candidate.get) 

#get output in string
output = f"""
Election Results
-----------------------------
Total Votes: {total_votes}
-----------------------------
"""
for candidate_name, votes in votes_per_candidate.items():
        output += f"{candidate_name}: {vote_percentage[candidate_name]:.3f}% ({votes})\n"
output += f"""
-----------------------------
Winner: {election_winner}
-----------------------------
"""

#print output
print(output)

#set path for output file
txtpath = r"analysis\results3.txt"
out_path = os.path.join(script_directory,txtpath)

with open(out_path, mode='w') as file:
    file.write(output)
    
        


  