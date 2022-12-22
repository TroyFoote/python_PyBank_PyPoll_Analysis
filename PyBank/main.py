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
profit_loss_change = 0 #total of differences between months profit and loss
ave_profit_loss_change = 0
greatest_increase_profits = 0
greatest_decrease_profits = 0


#import csv file from computer
budget_data_csv = os.path.join("Resources", "budget_data.csv")

#open csv file
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)
    
    #loop through csv
    for row in csv_reader:
        month_count +=1

        current_month_profit_loss = int(row[1])
        total_profit_loss += current_month_profit_loss
          
    #total months & profit loss totals included in report
    print(month_count)
    print(total_profit_loss)

    #changes in Profit/Loss per month over the full period
    for row in csv_reader:
        previous_month_profit_loss = int(row[1])
        profit_loss_change = current_month_profit_loss - previous_month_profit_loss
  
    
    print(profit_loss_change)
    print(current_month_profit_loss)
    
    










