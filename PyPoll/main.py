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
        
    #print election results        
    print(f"Election Results")    
    print(f"_________________________")
    print(f"Total Votes: {total_votes}") 
    print(f"_________________________")

    #percentage of votes per candidate
    for name in candidate_votes:
        votes = candidate_votes[name]
        percentage = votes / total_votes
        percent = round(percentage *100 ,3)

        #print results
        print(f"{name} : {percent}%, {votes}")

        #find winner
        if votes > win_votes:
            win_votes = votes
            winner = name

           
    
    #print winner results
    print(f"_________________________")

    print(f"Winner: {winner}")

    print(f"_________________________")


#output file to Analysis folder
output_file = os.path.join("Analysis", "Election_Analysis.txt")
with open(output_file, "w") as results:

    #write analysis report to txt file
    results.write("Election Results\n")
    results.write(f"____________________\n")
    results.write(f"Total Votes: {total_votes}\n") 
    results.write(f"_________________________\n")
    results.write(f"{name} : {percent}%, {votes}\n")
    results.write(f"_________________________\n")
    results.write(f"Winner: {winner}\n")
    results.write(f"_________________________\n")




     
    
    
    


        


