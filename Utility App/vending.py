class VendingMachine:
    def __init__(self):
        # Display items with categorie, code, name, price, and stock
        self.items = { 
            "Cold Drinks": {
                "C1": {"name": "Cold Starbucks Frappuccino Coffee", "price": 19.50, "stock": 8},
                "C2": {"name": "Pepsi", "price": 3.00, "stock": 10},
                "C3": {"name": "Sprite", "price": 3.00, "stock": 4},
            },
            "Snacks": {
                "S1": {"name": "Oman Chips", "price": 4.50, "stock": 5},
                "S2": {"name": "KitKat", "price": 1.80, "stock": 7}, 
                "S3": {"name": "Oreo Sandwich Cookies", "price": 25.50, "stock": 7}, 
            },
            "Healthy Options": {
                "H1": {"name": "Granola Bar", "price": 2.50, "stock": 4},
                "H2": {"name": "SunBites Olive & Oregano", "price": 3.50, "stock": 9},
                "H3": {"name": "Hunter's Gourmet Beetroot Chips", "price": 3.50, "stock": 5},

            }
        }

    def display_menu(self):
        print("\nWelcome to the GRAB AND GO Vending!") 
        print("Where your cravings meet instant satisfaction!")
        print("\nHere's what we have for you today:")
        for category, items in self.items.items():
            print(f"\n♦ {category}:")
            for code, details in items.items():
                print(
                    f"  {code}: {details['name']} - AED {details['price']:.2f} "
                    f"({details['stock']} in stock)"
                )

    def get_item(self, code):
        """Fetches item details by code."""
        for category in self.items.values():
            if code in category:
                return category[code]
        return None

    def prompt_user_for_selection(self):
        """Prompts user to select an item and validates the selection."""
        while True:
            user_input = input("\nEnter the item code (e.g., C1, C2, C3 | S1, S2, S3| H1, H2, H3 : ").upper()
            if user_input == "EXIT":
                return None, None
            item = self.get_item(user_input)
            if item:
                if item["stock"] > 0:
                    print(f"You selected: {item['name']} ✓") 
                    
                    return user_input, item
                else:
                    print(f" Sorry, {item['name']} is out of stock. Please choose another item.")
            else:
                print("❌ Invalid code. Please try again.")

    def prompt_for_payment(self, item_price):
        """Handles payment process and ensures sufficient payment is made."""
        while True:
            try:
                payment = float(input(f"The price is AED {item_price:.2f}. Enter payment: AED "))
                if payment >= item_price:
                    return payment
                else:
                    print("Insufficient payment. Please enter at least the item price.")
            except ValueError:
                print("❌ Invalid input. Please enter a numeric value.")

    def calculate_change(self, payment, item_price):
        """Calculates change to be returned."""
        return round(payment - item_price, 2)

    def suggest_items(self, purchased_item_code):
        """Suggests additional items, excluding the purchased item."""
        suggestions = []
        for category, items in self.items.items():
            for code, details in items.items():
                if code != purchased_item_code and details["stock"] > 0:
                    suggestions.append(details["name"])
        return suggestions[:2]  # Suggest up to 2 items

    def run(self):
        """Main method to execute the vending machine process."""
        while True:
            self.display_menu()  # Display available items

            # Prompt user for item selection
            selected_code, item = self.prompt_user_for_selection()
            if not selected_code:
                print("\nThank you for using the Vending Machine. Goodbye!")
                break

            # Handle payment
            payment = self.prompt_for_payment(item["price"])

            # Calculate and return change
            change = self.calculate_change(payment, item["price"])
            print(f"\n ✔ Dispensing {item['name']}... Enjoy!")
            if change > 0:
                print(f"↩ Returning AED {change:f} in change.")

            # Update stock
            item["stock"] -= 1

            # Suggest additional items
            suggestions = self.suggest_items(selected_code)
            if suggestions:
                print(f"\n How about trying: {', or  '.join(suggestions)}?")

            # Ask if the user wants to purchase another item
            continue_choice = input("\nWould you like to purchase another item ? (yes/no): ").lower()
            if continue_choice != "yes":
                print("\nThank you for using the Vending Machine. Goodbye!")
                break


if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.run()
