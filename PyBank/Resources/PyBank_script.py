#Dependeces
import os
import csv

#create a function to print both the results on terminal and a .txt file
def print_analysis(row_count, net_amount, date_max,date_min, avg_diff, maxvalue,minvalue):
    fp_write = open('Analysis.txt', 'w')
    # # fp_write("text")
    print('text')
    fp_write.write('text\n')
    print('Financial Analysis')
    fp_write.write(f'Financial Analysis\n')
    print(f'------------------------------')
    fp_write.write('------------------------------\n')
    print(f'Total Months: {row_count}')
    fp_write.write(f'Total Months: {row_count}\n')
    print(f'Total: ${net_amount}')
    fp_write.write(f'Total: ${net_amount}\n')
    print(f'Average change: ${avg_diff}')
    fp_write.write(f'Average change: ${avg_diff}\n')
    print(f'Greatest Increase in Profits: {date_max} (${maxvalue})')
    fp_write.write(f'Greatest Increase in Profits: {date_max} (${maxvalue})\n')
    print(f'Greatest Decrease in Profits: {date_min} (${minvalue})')
    fp_write.write(f'Greatest Decrease in Profits: {date_min} (${minvalue})\n')


## Open and read csv
path = os.path.join('.', 'Resources', 'budget_data.csv')
with open(path) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    # Read the header row first
    csv_header = next(reader)
    #Read the second row right after setting the variables necessaries to find
    #months, total net amount, change in profit and loss, greatest increase and decrease

    #Reading row 2
    row = next(reader)
    row_count = 1
    maxvalue = 0
    minvalue = 0
    date_max = 0
    date_min = 0
    net_amount = int(row[1])
    previous_value = int(row[1])
    sum_diff_value = 0

    # Read through the rows starting at row 3:
    for row in reader:
        #calculate the months by considering the number of rows
        row_count += 1
        #calculate the total net amount of Profit/Losses after converting row to int
        current_value = int(row[1])
        net_amount += current_value
        #calculate the change between the new value and the old value (current value and previous)
        diff_value = current_value - previous_value
        sum_diff_value += diff_value
        previous_value = current_value
        #find the average of all changes (considering we have 85 values, not 86)
        avg_diff = round(sum_diff_value / (row_count-1),2)
        # Compare the rows to find the greatest increase and decrease in profit through a
        #conditional statement
        if diff_value > maxvalue:
            maxvalue = diff_value
            date_max = row[0]
        if diff_value < minvalue:
            minvalue = diff_value
            date_min = row[0]

#Commenting out the original code used to create the function
    # print("text")
    # print("Financial Analysis")
    # print("------------------------------")
    # print(f'Total Months: {row_count}')
    # print(f'Total: ${net_amount}')
    # print(f'Average change: ${avg_diff}')
    # print(f'Greatest Increase in Profits: {date_max} (${maxvalue})')
    # print(f'Greatest Decrease in Profits: {date_min} (${minvalue})')

#call the function to print on the terminal and create a .txt file
print_analysis(row_count, net_amount, date_max,date_min, avg_diff, maxvalue,minvalue)
