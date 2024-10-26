# Making the list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

search_name = input("Enter a name to search for: ") #Letting the user search for Sam

#Using if else to determine whether Sam is in the list or not.

if search_name.lower() in [name.lower() for name in names]: # Check if name is in the list (case insensitive)
    print(search_name.capitalize(), "is in the list.") # Using capitalize() to write the proper name
else:
    print(search_name.capitalize(), "is not in the list.")