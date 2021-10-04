#The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candiate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote

#Add dependencies
import csv
import os
path = "/Users/mthal/Desktop/UofO/Bootcamp/Mod_3/Mod_3_Work/Election_Analysis"
#Assign a variable for the file to load and the path.
file_to_load = os.path.join(path, "Resources", "election_results.csv")
#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter
total_votes = 0

#Declare a candidate list
candidate_options = []

#Declare the empty dictionary
candidate_votes = {}

#Open the election results and read the file.
with open(file_to_load) as election_data:

    #To do: read and analyze data
        #print(election_data)

    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Print the header row.
    headers = next(file_reader)
    #for row in file_reader:
        #print(headers)

    #Print each row in the csv file.
    for row in file_reader:
        #Add to the total vote count
        total_votes += 1
        #print(row)

        #print the candidate name from each row
        candidate_name = row[2]

        #If candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            #add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            #begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        #Add vote to that candidate's count
        candidate_votes[candidate_name] += 1

    #determine the percentage of votes for each candidate by looping through the counts
    for candidate_name in candidate_votes:
        #retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #calculate the percentage of votes
        vote_percentage = round(float(votes) / float(total_votes) * 100, 2)


        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        #determine the winning vote count and candidate
        #determine if the votes are greater than the winning count
        
        if (votes > winning_count) and (vote_percentage > winning_percentage):
                #if true then set winning_count = votes and winning_percent = vote percentage
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
                #set the winning_candidate equal to the candidates name
    winning_candidate_summary = (
        f"----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------------\n")
    print(winning_candidate_summary)
