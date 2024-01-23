import csv
import os

def financial_analysis(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)

        # Explining of the varaible 
        total_months = 0
        net_total = 0
        previous_profit_loss = 0
        changes = []
        greatest_increase = {"date": "", "amount": float('-inf')}
        greatest_decrease = {"date": "", "amount": float('inf')}

        # Looping through the csv file rows 
        for row in reader:
            total_months += 1
            net_total += int(row["Profit/Losses"])
            current_profit_loss = int(row["Profit/Losses"])
            if total_months > 1:
                change = current_profit_loss - previous_profit_loss
                changes.append(change)

        # Update greatest increase and decrease
                if change > greatest_increase["amount"]:
                    greatest_increase["date"] = row["Date"]
                    greatest_increase["amount"] = change

                if change < greatest_decrease["amount"]:
                    greatest_decrease["date"] = row["Date"]
                    greatest_decrease["amount"] = change

        # Update previous Profit/Loss value
            previous_profit_loss = current_profit_loss

        # Calculate average of changes
        average_change = sum(changes) / len(changes)

        # Print the final result 
        print("Financial Analysis")
        print("----------------------------")
        print(f"Total Months: {total_months}")
        print(f"Net Total: ${net_total}")
        print(f"Average Change: ${average_change:.2f}")
        print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
        print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")

# Provide the path to your CSV file
csv_file_path = os.path.join("PyBank/Resources","budget_data.csv")

# Print the functions to analyze the financial data
financial_analysis(csv_file_path)