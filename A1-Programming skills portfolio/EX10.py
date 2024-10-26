


def even_odd(num): # Creating a function to check even or odd numbers!
    if (num % 2) == 0:
        return f"{num} is even."  
    
    else:                           # Using return to indicate whether the number is even or odd.
        return f"{num} is odd."   


def main(): # Getting the user input in the main function.
    num = int(input("Enter a number: ")) 
    result = even_odd(num)                 
    print(result) # Printing the return message within the main function.


main()