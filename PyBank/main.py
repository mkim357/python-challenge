# $ /usr/bin/python3 ./PyBank/main.py

import csv

# Define the path to the CSV file

file_path = "PyBank/Resources/budget_data.csv"

# Initialize variables

total_months = 0
net_total = 0
previous_month_profit = None
changes = []
dates = []

# open and read CSV file

with open(file_path, "r") as csvfile:
    csvreader = csv.reader(csvfile)

    # read the header
    header = next(csvreader)

    # loop through each row in CSV

    for row in csvreader:
        date = row[0]
        profit_loss = int(row[1])

        # track the dates for reference in changes
        dates.append(date)

        # update total number of months
        total_months += 1

        # update net total amount of "Profit/Losses"
        net_total += profit_loss

        # calculate the monthly change in profit/losses
        if previous_month_profit is not None:
            change = profit_loss - previous_month_profit
            changes.append(change)

        # set the previous month's profit/loss for the next iteration
        previous_month_profit = profit_loss

# calculate the average change in "Profit/Losses"
average_change = sum(changes) / len(changes)

#find the greatest increase and decrease in profits
greatest_increase = max(changes)
greatest_decrease = min(changes)
greatest_increase_date = dates[changes.index(greatest_increase) +1]
greatest_decrease_date = dates[changes.index(greatest_decrease) +1]

# print the analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
