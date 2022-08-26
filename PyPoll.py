#import project dependencies
#import CSV module
import csv

#import os module
import os

#Load the file to read by giving the direct file path
file_to_load = ("Resources/election_results.csv")

#write to the file by providing the direct file path
file_to_save = ("Analysis/election_analysis.txt")

#initialize the total votes count variable to zero.
total_votes = 0

#initialize the candidates list to zero.
candidates_list = []

#intialize an empty dictionaty
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


#open the file to read assign to a file variable
with open(file_to_load) as election_data:

    #create a file object using csv reader
    file_reader = csv.reader(election_data)

    #header row
    #remove the header row to count the total votes cast
    headers = next(file_reader)

    #iterate over each row to count the total votes
    for row in file_reader:
        total_votes +=1
        #print(total_votes)

        #candidate name in each row
        candidate_name = row[2]
        
        #add the candidate name if it is not in the list
        if candidate_name not in candidates_list:
            #add it to the list of candidates
            candidates_list.append(candidate_name)
            #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
#print(candidates_list)
print(candidate_votes)

#determine the percentage of votes for each candidate
for candidate_name in candidate_votes:
    
        #find the vote count for each candidate
        votes = candidate_votes[candidate_name]

        #calculate the percentage of votes
        percentage_votes = (votes/total_votes)*100

        #print the candidate name and percentage of votes
        print(f"{candidate_name} : recieved {percentage_votes:.1f}% ({votes})\n")

        #determine winning vote count and winning candidate
        if (votes > winning_count) and (percentage_votes > winning_percentage):

                #get the votes for the candidate and set it to winning count
                winning_count = votes

                #get the percentage of votes and set it to winning percentage
                winning_percentage = percentage_votes

                #set the candidate name as the winning candidate 
                winning_candidate =  candidate_name

#print the winning candidate
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)


