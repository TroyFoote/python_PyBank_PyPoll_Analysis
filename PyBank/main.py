# Pybank Script

# #import os module
import os

#import csv module
import csv

#variables
total = 0
month_count = 0
profit_loss_net = 0
profit_loss_change = []
ave_profit_loss_change = 0
greatest_increase_profits = 0
greatest_decrease_profits = 0

#import csv file from computer
budget_data_csv = os.path.join("Resources", "budget_data.csv")

#open csv file
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)
    #print(f"Header: {csv_header}")

    for row in csv_reader:
        month_count +=1
        

    print(month_count)







    

