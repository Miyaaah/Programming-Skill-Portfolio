# Defining the correct password
correct_password = "12345" 

# Setting the number of attempts
max_attempts = 5
attempts = 0

# Ask the user for the password with a limit on attempts
while attempts < max_attempts:
    password = input("Password: ")  # Using a string for the password to handle any input
    
    if password == correct_password:
        # If the password is correct
        print("Password Correct!")
        break  # Exit the loop if the password is correct
    else:
        attempts += 1  # Increment the attempt counter
        remaining_attempts = max_attempts - attempts  # Calculate remaining attempts
        print("Try again. You have", remaining_attempts,"attempt/s left." )  # Inform the user of remaining attempts

# If the maximum number of attempts is reached
if attempts == max_attempts:
    print("Maximum attempts reached. Authorities have been alerted.")