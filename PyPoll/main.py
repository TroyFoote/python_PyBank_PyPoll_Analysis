#Pypoll Script

#import os module
import os

#import csv module
import csv

#Variables
total_votes = 0 #total votes cast
candidate_list = []
#percent_votes_candidate = 0
candidate_votes = {}
winner = ""
win_votes = 0
win_percent = 0

#import csv file from computer
election_data_csv = os.path.join("Resources", "election_data.csv")

#open csv file
with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    

    #loop through csv
    for row in csv_reader:
        total_votes +=1
        candidate_name = row[2]

        #create list of candidates and votes per candidate
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_votes[candidate_name]= 0
        candidate_votes[candidate_name]+=1

    output_candidates = ""    
    #percentage of votes per candidate
    for name in candidate_votes:
        votes = candidate_votes[name]
        percentage = votes / total_votes
        percent = round(percentage *100 ,3)
        output_candidates += f"{name} : {percent}%, {votes}\n"
        #find winner
        if votes > win_votes:
            win_votes = votes
            winner = name
    
    output_text = (      
    f"Election Results\n"    
    f"_________________________\n"
    f"Total Votes: {total_votes}\n" 
    f"_________________________\n"
    f"{output_candidates}"
    f"_________________________\n"
    f"Winner: {winner}\n"
    f"_________________________\n"
    )
    print(output_text, end="")

#output file to Analysis folder
output_file = os.path.join("Analysis", "Election_Analysis.txt")
with open(output_file, "w") as results:
    results.write(output_text)


 




     
    
    
    


        


