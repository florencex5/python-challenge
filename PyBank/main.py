# Import the os module
import os

# Module for reading CSV files
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')

# List the data
monthly_changes_PL=[]

#Set the initial value
months_count = 0
current_month_PL = 0
last_month_PL = 0
Total_PL = 0
monthly_change_PL = 0
highest_month=""
lowest_month=""
greatest_increase_PL=0
greatest_decrease_PL=0

# Read in the CSV file
with open(budget_csv, encoding= 'UTF-8' ) as csvfile:
    
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read and print the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
   
    # Read each row of data after the header
    for row in csvreader:
        
        #Calculate the total number of months and the total p&l over the entire period
        months_count += 1
        current_month_PL = int(row[1])
        Total_PL += current_month_PL
        
        #Set up the zero change for the first month
        if months_count == 1 :
            last_month_PL = current_month_PL
        else:
            #Calculate monthly change p&l over the entire period
            monthly_change_PL = current_month_PL - last_month_PL
        
            #Add montly changes
            monthly_changes_PL.append(monthly_change_PL)
        
            #Determine the last month p&l for the next loop 
            last_month_PL = current_month_PL
            
            # Calculate the average monthly change p&l over the entire period
            total_monthly_changes_PL = sum(monthly_changes_PL)
            average_monthly_changes_PL = round (total_monthly_changes_PL/(months_count-1),2)
            
            # Calculate the greatest increase/decrease in p&l and determine the highest/lowest month over the entire period
            if monthly_change_PL > greatest_increase_PL:
                greatest_increase_PL = monthly_change_PL
                highest_month = row[0]
            elif monthly_change_PL < greatest_decrease_PL:
                    greatest_decrease_PL = monthly_change_PL 
                    lowest_month = row[0]

# Print out the final analysis results to the terminal
print(f"Total Months: {months_count}")
print(f"Total: ${Total_PL}")
print(f"Average Change: ${average_monthly_changes_PL}")
print(f"Greatest Increaes in Profits: {highest_month} (${greatest_increase_PL})")
print(f"Greatest Decrease in Profits: {lowest_month} (${greatest_decrease_PL})")

# Set variable for output analysis file
pybank_file = os.path.join('Analysis',"pybank_analysis.txt")

# Open the output file
with open(pybank_file, "w") as text:

    # Print the analysis results in the output analysis file
    text.write("Financial Analysis\n")
    text.write("--------------------------------------\n")
    text.write(f"Total Months: {months_count}\n")
    text.write(f"Total: ${Total_PL}\n")
    text.write(f"Average Change: ${average_monthly_changes_PL}\n")
    text.write(f"Greatest Increaes in Profits: {highest_month} (${greatest_increase_PL})\n")
    text.write(f"Greatest Decrease in Profits: {lowest_month} (${greatest_decrease_PL})\n")