# Pypoll Script

# #import os module
import os

#import csv module
import csv

#Variables
total_votes = 0 #total votes cast
candidate_list = []
percent_votes_candidate = 0
candidate_votes = 0
winner = []
candidate_list = ["Charles Casper Stockham","Diana DeGette","Raymon Anthony Doane" ]
candidate1 = {
  "name" : "Charles Casper Stockham",
  "votes" : 0
  }
candidate2 = {
  "name" :"Diana DeGette",
  "votes" : 0
}
candidate3 = {
  "name" : "Raymon Anthony Doane",
  "votes" : 0
}
candidates ={
    "candidate1" : candidate1,
    "candidate2" : candidate2,
    "candidate3" : candidate3
}
print(candidates)

candidate_list = candidates
print(candidate_list)

#import csv file from computer
election_data_csv = os.path.join("Resources", "election_data.csv")

#open csv file
with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)

#loop through csv
    for row in csv_reader:
        total_votes +=1
        
        #candidate_votes = (row[2])
      



print(total_votes)
print(candidate_votes)

#print(candidate_list)
#print(candidates)