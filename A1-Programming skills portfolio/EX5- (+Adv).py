# Creating a dictionary where the keys are month numbers and the values are the number of days in those months.

months = {1:31,
         2:28,
         3:31 ,
         4:30,
         5:31 ,
         6:30,
         7:31 ,
         8:31 ,
         9:30 ,
         10:31,
         11:30,
         12:31}

month_num = int(input("Enter any month number (1-12): ")) # Get user input for the month number

if month_num in months: #Check if the user's input is a valid month number in the dictionary.
    if month_num == 2:
        leap_year = input("Is it a leap year? (yes/no): ") #In case the user is referring to febuary leap year.
        
        if leap_year == 'yes':
            print("February has 29 days in a leap year.")
        else:
            print("February has", months[2], "days")
    else: # For the rest of the other months
        print("The month has", months[month_num],"days.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")
