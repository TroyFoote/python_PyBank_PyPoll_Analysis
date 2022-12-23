# Pybank Script

# #import os module
import os

#import csv module
import csv

#variables
month_count = 0 #total months
current_month_profit_loss = 0 
total_profit_loss = 0 #all months added together
previous_month_profit_loss = 0
total_profit_loss_change = 0 #total of differences between months profit and loss
greatest_increase_profits = 0
greatest_decrease_profits = 0
change_count = 0
first_row = True

#import csv file from computer
budget_data_csv = os.path.join("Resources", "budget_data.csv")

#open csv file
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_reader)
    
    #loop through csv
    for row in csv_reader:
        month_count +=1
        current_month_profit_loss = int(row[1])
        total_profit_loss += current_month_profit_loss

        if first_row:    
            first_row = False   
        else: 
            change_count +=1
            current_profit_loss_change = current_month_profit_loss - previous_month_profit_loss
            total_profit_loss_change += current_profit_loss_change
        previous_month_profit_loss = current_month_profit_loss

    ave_profit_loss_change = round(total_profit_loss_change / change_count, 2)

    #total months & profit loss totals included in report
    print(month_count)
    print(total_profit_loss)
     
    
    print(total_profit_loss_change)
    print(current_month_profit_loss)
    print(change_count)
    print(ave_profit_loss_change)
    
    










