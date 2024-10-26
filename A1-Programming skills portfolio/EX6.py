
 # Defining the correct password
correct_password = "12345" 


password = input("Password: ") # Using a string for the password to handle character input

# Ask the user for the password multiple times using a while loop until they enter the right one
while password != correct_password:
    print("Try again")  # Print "Try again" on one line
    password = input("Password: ")  

# If the password is correct
print("Password Correct!")