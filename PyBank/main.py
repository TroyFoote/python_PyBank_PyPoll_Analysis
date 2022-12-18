#import os
import os

#import csv
import csv

#import csv file from computer
budget_data_csv = os.path.join("Resources", "budget_data.csv")

#open csv file
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)
    print(f"header: {csv_header}")

    

