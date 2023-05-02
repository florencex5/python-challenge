# Import the os module
import os

# Module for reading CSV files
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'election_data.csv')

# Create a dictionary for all candidates
cand_dict={"Charles Casper Stockham": 0, "Diana DeGette": 0, "Raymon Anthony Doane": 0}

#Set the initial value of items
total_votes = 0
maximum = 0
name_maximum = ''

# Read in the CSV file
with open(budget_csv, encoding= 'UTF-8' ) as csvfile:
    
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read and print the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
       
    # Read each row of data after the header
    for row in csvreader:
        
        #Calculate the total number of votes
        total_votes += 1
        
        #Calculate the total number of votes for each candidate
        cand_dict[row[2]] += 1

#Find the winner
for name in cand_dict:

    if cand_dict[name] / total_votes > maximum:
        maximum = cand_dict[name] / total_votes
        name_maximum = name

#Print out the total votes to the terminal
print(f"Total Votes: {total_votes}")

#Print out the complete list of each candidate with name, number of votes and percentage of votes to the terminal
for name in cand_dict:
    print(f"{name} : {format(cand_dict[name]/ total_votes,'.3%')} ({cand_dict[name]})")

#Print out the name of winner to the terminal
print(f"Winner: {name_maximum}") 

# Set variable for output analysis file
pypoll_file = os.path.join('Analysis',"pypoll_analysis.txt")

# Open the output file
with open(pypoll_file, "w") as text:

    # Print the analysis results in the output analysis file
    text.write("Election Results\n")
    text.write("--------------------------------------\n")
    text.write(f"Total Votes: {total_votes}\n")
    text.write("--------------------------------------\n")
    for name in cand_dict:
        text.write(f"{name} : {format(cand_dict[name]/ total_votes,'.3%')} ({cand_dict[name]})\n")
    text.write("--------------------------------------\n")
    text.write(f"Winner: {name_maximum}\n")
    text.write("--------------------------------------\n")