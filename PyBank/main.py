# Pybank Script

# #import os module
import os

#import csv module
import csv

#variables
months = []
profit_loss_changes = []
month_count = 0 #total months
current_month_profit_loss = 0 
total_profit_loss = 0 #all months added together
previous_month_profit_loss = 0
total_profit_loss_change = 0 #total of differences between months profit and loss
change_count = 0
first_row = True




#import csv file from computer
budget_data_csv = os.path.join("Resources", "budget_data.csv")

#open csv file
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
    
    #loop through csv to find total number of months
    for row in csv_reader:
        month_count +=1

        #find total profit/loss     
        current_month_profit_loss = int(row[1])
        total_profit_loss += current_month_profit_loss

        #find change in profit/loss between current and previous months
        if first_row:    
            first_row = False   
        else: 
            change_count +=1
            current_profit_loss_change = current_month_profit_loss - previous_month_profit_loss
            total_profit_loss_change += current_profit_loss_change
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss

            #create lists for profit loss changes and months
            profit_loss_changes.append(profit_loss_change)
            months.append(row[0])

            #find greatest increase/decrease in profits
            greatest_increase_profit_loss = max(profit_loss_changes)
            greatest_decrease_profit_loss = min(profit_loss_changes)

            #find month that matches greatest increase/decrease in profits           
            greatest_increase_month = profit_loss_changes.index(greatest_increase_profit_loss) 
            greatest_decrease_month = profit_loss_changes.index(greatest_decrease_profit_loss) 
            highest_month = months[greatest_increase_month]
            lowest_month = months[greatest_decrease_month]

        #hold current month profit loss for next loop
        previous_month_profit_loss = current_month_profit_loss

    #find the average change in profit/loss between current and previous months
    ave_profit_loss_change = round(total_profit_loss_change / change_count, 2)



    #print analysis report
    print("Financial Analysis")
    print("_____________________________________")
    print(f"Total Months: {month_count}")
    print(f"Total: ${total_profit_loss}")
    print(f"Total Change: ${total_profit_loss_change}")
    print(f"Average Change: ${ave_profit_loss_change}")
    print(f"Greatest Increase in Profits: {highest_month } ${greatest_increase_profit_loss}")
    print(f"Greatest Decrease in Profits: {lowest_month } ${greatest_decrease_profit_loss}")

    
#output file to Analysis folder
output_file = os.path.join("Analysis", "Final_Analysis.txt")
with open(output_file, "w") as results:

    results.write("Financial Analysis\n")
    results.write("_____________________________________\n")
    results.write(f"Total Months: {month_count}\n")
    results.write(f"Total: ${total_profit_loss}\n")
    results.write(f"Total Change: ${total_profit_loss_change}\n")
    results.write(f"Average Change: ${ave_profit_loss_change}\n")
    results.write(f"Greatest Increase in Profits: {highest_month } ${greatest_increase_profit_loss}\n")
    results.write(f"Greatest Decrease in Profits: {lowest_month } ${greatest_decrease_profit_loss}\n")   
    


      
    
    
    
    
    
    #total months & profit loss totals included in report
    #print(month_count)
    #print(total_profit_loss)   
    #print(total_profit_loss_change)
    
    #print(current_month_profit_loss)
    #print(change_count)
    
    #print(ave_profit_loss_change)
    #print(profit_loss_changes)
    #print(months)
    #print(greatest_increase_profit_loss)
    #print(greatest_decrease_profit_loss)
    #print(highest_month)
    #print(lowest_month)
