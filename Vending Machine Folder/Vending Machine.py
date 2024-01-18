# Dictionary that has the menu for the vending machine
def items_vending_machine_menu():
    return {
        1: {"item": "Orange Juice", "Price": 3.50},
        2: {"item": "Apple Juice", "Price": 3.50},
        3: {"item": "Coca Cola", "Price": 4},
        4: {"item": "Mountain Dew", "Price": 4},
        5: {"item": "Chocolate Drink", "Price": 3},
        6: {"item": "Chocolate Croissant", "Price": 3},
        7: {"item": "Cupcake", "Price": 1.50},
        8: {"item": "Cookie", "Price": 1.50},
        9: {"item": "Chips", "Price": 2},
        10: {"item": "Ice Cream Sandwich", "Price": 2.50}
    }

# Function to display the vending machine menu
def display_menu(menu):
    print ("\n")
    print ("Welcome to the Vending Machine!\n")
    print ("Menu:")
    for key, item in menu.items():
        print(f"{key}. {item['item']} - {item['Price']:.2f} DHS")

# Function to select an item from the menu
def select_item(menu):
    while True:
        try:
            choice = int(input("\nPlease enter the number of your selection (1-10): "))
            if choice in menu:
                return choice
            else:
                print("Invalid selection. Please enter a valid number (1-10).")
        except ValueError:
            print("Invalid input. Please enter a number from 1-10.")

# Function to process payment for the selected item
def process_payment(price):
    while True:
        try:
            amount = float(input("Enter the amount of money in AED: "))
            if amount >= price:
                return amount
            else:
                print("Insufficient funds. Please enter a sufficient amount.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

# Main function to simulate the vending machine operation
def vending_machine():
    menu = items_vending_machine_menu()
    display_menu(menu)

    while True:
        # Select an item from the menu
        choice = select_item(menu)
        selected_item = menu[choice]
        price = selected_item['Price']
        
        # Display the selected item and its price
        print(f"\nYou have selected: {selected_item['item']} - {price:.2f} AED")
        
        # Process payment for the selected item
        amount_paid = process_payment(price)
        
        # Calculate change and provide a message to the user
        change = amount_paid - price
        if change > 0:
            print(f"\nThank you for your purchase! Enjoy your {selected_item['item']} and your change of AED {change:.2f}!")
        else:
            print(f"\nThank you for your purchase! Enjoy your {selected_item['item']}!")

        # Ask if the user wants to make another purchase
        another_purchase = input("\nDo you want to make another purchase? (Yes/No): ")
        if another_purchase.lower() != "yes":
            print("Thank you for using the vending machine. Have a great day!\n")
            break

# Call the vending machine function to start the simulation
vending_machine()
