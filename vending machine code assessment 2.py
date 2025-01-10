import sqlite3

def sales_data(item_name, price, quantity_sold):
    """Insert sales data into the database."""
    try:
        conn = sqlite3.connect(r'C:/Users/hp/Desktop/Assesment 2/A2DB.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO items (item, price) 
            VALUES (?, ?)
        ''', (item_name, price)) 
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error with database operation: {e}")
    finally:
        conn.close()

def display_items(items):
    """Display available items and their prices."""
    print("---SELECT ITEMS---\n")
    for item_code, (item_name, price) in items.items():
        print(f'{item_code} : {item_name}, {price:.2f} AED')

def get_user_choice(items):
    """Get the user's choice of item."""
    while True:
        choice = input("Please select what you would like (or type 'exit' to quit): ").upper().strip()
        if choice == 'EXIT':
            print("Exiting the vending machine. Have a nice day!")
            return None
        if choice not in items:
            print("This is not a valid option, please try again.")
        else:
            return choice

def process_payment(price):
    """Handles the payment process, including multiple attempts and change calculation."""
    while True:
        try:
            money_input = input(f"Please insert the required amount of money ({price:.2f} AED): ").strip()
            if money_input.lower() == 'exit':
                print("Exiting the vending machine. Have a nice day!")
                return None
            money = float(money_input)
            if money < price:
                print(f"Insufficient funds. You need {price - money:.2f} more AED.")
            else:
                change = money - price
                if change > 0:
                    print(f"Thank you for your purchase! Your change is {change:.2f} AED.")
                else:
                    print("Thank you for your purchase! No change required.")
                return change
        except ValueError:
            print("Invalid input. Please enter a valid number for money.")

def main():
    # List of items available in the vending machine
    items = {
        "150": ("Coke", 3.50),
        "151": ("Fanta", 3.50),
        "152": ("Takis", 2.00),
        "153": ("Lays", 3.00),
        "154": ("Cheetos", 5.00),
    }

    # Display items to the user
    display_items(items)

    # Get user's selection
    choice = get_user_choice(items)

    if choice:
        item_name, price = items[choice]  
        # Ask for the quantity of items
        while True:
            try:
                quantity = int(input(f"How many {item_name}s would you like to buy? "))
                if quantity <= 0:
                    print("Please enter a quantity greater than zero.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number for quantity.")
        
        total_price = price * quantity
        print(f"The total price for {quantity} {item_name}(s) is {total_price:.2f} AED.")

        # Process payment and handle change
        change = process_payment(total_price)
        if change is not None:
            print("Thank you for your purchase! Have a nice day!")
            print(f"Your change is {change:.2f} AED.")

            # Record the sale in the database
            sales_data(item_name, price, quantity)

if __name__ == "__main__":
    main()

