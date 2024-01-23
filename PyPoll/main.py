import csv
import os

#Explain path to the CSV file for runing the code 
csv_filename = 'election_data.csv'
csvfile_path = os.path.join("PyPoll/Resources", csv_filename)

#Defining the Varibles of the CSV file to analysis 
total_votes = 0
candidate_name_list = []

#Open and read the CSV file 
with open(csvfile_path,'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)
    row_counter = 1

    # looping through the rows on the file 
    for row in csv_reader:
        total_votes += 1

        # Take candidate name from the row 
        candidate_name = row[2]
        candidate_name_list.append(candidate_name)
        
print("Election-Results")
print("--------------------------------------------")
print(f"Total votes: {total_votes}")


votes_list=[]
winner_list=[]  
candidate_unique_names = list(set(candidate_name_list)) 

# looping through candidates unique names and counting them
for candidate in candidate_unique_names:
    votes = candidate_name_list.count(candidate)
    #Create vote and winner list 
    votes_list.append(votes)
    winner_list.append(candidate)
    percentage = votes / total_votes * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    
# Finding the Max vote and announcing the winner 
Winner_vote = max(votes_list)
position = votes_list.index(Winner_vote)
Winner_candidate = winner_list[position]
print(f"The winner is: {Winner_candidate} and has won {Winner_vote} votes.")