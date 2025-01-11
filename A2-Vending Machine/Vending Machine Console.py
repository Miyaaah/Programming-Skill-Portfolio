"""Vending machine"""

# Creating dictionary of items and the price for the machine.
menu = {
    "Snacks": {
        "1A": ("Twix", 3.00),
        "1B": ("Potato Chips", 5.00),
        "1C": ("Snickers", 3.00),
        "1D": ("Biscuits", 2.00),
        "1E": ("Energy Bar", 1.00)
    },
    "Drinks": {
        "2A": ("Water", 0.50),
        "2B": ("Pepsi", 3.00),
        "2C": ("Lipton Ice Tea", 4.00),
        "2D": ("Energy Drink", 4.00),
        "2E": ("Cold Coffee", 3.00)
    },
    "Coffee": {
        "3A": ("Cappuccino", 3.00),
        "3B": ("Americano", 2.50),
        "3C": ("Latte", 3.50),
        "3D": ("Mocha", 4.00),
        "3E": ("Black Coffee", 2.00)
    }
}

# Design of the vending machine
print(
    "======== Vending Machine ========",
    "Product        Price          Code ",
    "  ",
    "Twix           3.00$           1A",
    "Potato Chips   5.00$           1B",
    "Snickers       3.00$           1C ",
    "Biscuits       2.00$           1D   ",
    "Energy Bar     1.00$           1E  ",
    "  ",
    "==========",
    "  ",
    "Water          0.50$           2A",
    "Pepsi          3.00$           2B",
    "Lipton         4.00$           2C",
    "Energy Drink   4.00$           2D",
    "Cold Coffee    3.00$           2E",
    "  ",
    "==========",
    "  ",
    "Cappuccino     3.00$           3A",
    "Americano      2.50$           3B",
    "Latte          3.50$           3C",
    "Mocha          4.00$           3D",
    "Black Coffee   2.00$           3E",
    "==========",
    "  ",
    sep="\n",
)

user_balance = 20.00

# State how much balance the user has.
print("You have 20.00$")

selected_items = []
total_cost = 0.00

# Get input from user.
while True:
    code = input("Enter code (Type OK if done): ")

    if code.upper() == "OK":  # Check if the user is done
        break

    # A function for selecting items
    def selection(code):
        for category, items in menu.items():
            if code in items:  # Check if the code exists
                item_name = items[code][0]  # Get the item name
                item_price = items[code][1]  # Get the item price
                selected_items.append(item_name)  # Store the item name
                return item_price  # Return the item price
        print("Invalid code. Please try again.")
        return 0  # Return 0 for invalid code

    item_price = selection(code)  # Call the selection function
    if item_price > 0:  # Only update the total cost if valid item was selected
        total_cost += item_price
        print(f"You have selected: {', '.join(selected_items)}")  # Show user the selected items

def suggest():
    # Check if any selected items are from the Coffee category and no snacks are selected
    coffee_selected = any(item in selected_items for item in [menu["Coffee"][key][0] for key in menu["Coffee"]])
    snacks_selected = any(item in selected_items for item in [menu["Snacks"][key][0] for key in menu["Snacks"]])

    if coffee_selected and not snacks_selected:
        while True:
            response = input("Would you like Biscuits or Twix with your coffee? (yes/no): ")
            if response.lower() in ["yes", "no"]:
                break  # Exit the loop if the response is valid
            else:
                print("Invalid input. Please type 'yes' or 'no'.")

        if response.lower() == "yes":
            while True:
                snack_code = input("Enter code for Biscuits (1D) or Twix (1A): ")
                snack_price = selection(snack_code)  # Call selection to add the snack

                if snack_price > 0:
                    print(f"You have added: {snack_code} to your order.")
                    break  # Exit the loop if a valid snack code is entered
                else:
                    print("Invalid code. Please try again.")  

# Show purchase suggestion before paying IF user ordered items from coffee only, or coffee and drink category.
suggest()

# A preview of the final selected items and the total price
def preview():
    print("\nYou selected:", ", ".join(selected_items))
    print(f"Total is: {total_cost:.2f}$")

# Show the receipt before asking for payment
preview()

# Payment
while True:
    user_balance_input = float(input("Input your money: "))

    # Check if the input exceeds the available balance
    if user_balance_input > user_balance:
        print("You only have 20.00$ in your balance.")
    elif user_balance_input < total_cost:
        print("You don't have enough funds for this transaction.")
    else:
        break  # Exit the loop if the input is valid
        
        
# A function for the receipt
def receipt():
    if user_balance_input > total_cost:
        change = user_balance_input - total_cost
        print(" ")
        print("===================")
        print("===- RECEIPT -===")
        print(" ")
        print("Items bought:", ", ".join(selected_items))
        print(f"You paid: {user_balance_input:.2f}$")
        print(f"Change: {change:.2f}$")
        print("===================")
        print(" ")
        print("Thank you for your purchase!")
    elif user_balance_input == total_cost:
        print(" ")
        print("===================")
        print("===- RECEIPT -===")
        print(" ")
        print("Items bought:", ", ".join(selected_items))
        print(f"You paid: {user_balance_input:.2f}$")
        print("Change: 0.00$")
        print(" ")
        print("===================")
        print(" ")
        print("Thank you for your purchase!")
    else:
        print("Insufficient funds. Transaction canceled.")

receipt()

