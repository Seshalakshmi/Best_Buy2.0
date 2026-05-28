from products import Product
import store


def list_of_products_in_store(store_items):
    """Display all available products in the store.

        Args:
            store_items (store.Store): Store instance containing products.

        Prints:
            Enumerated list of products with details.
    """
    all_products = store_items.get_all_products()
    for nos, item in enumerate(all_products, 1):
        print(f"{nos}: {Product.show(item)}")
    print("________")


def total_stock_quantity(store_items):
    """Display the total quantity of items available in the store.

        Args:
            store_items (store.Store): Store instance containing products.
    """
    print(f"Total of {store_items.get_total_quantity()} items in store")


def make_order(store_items):
    """Handle the order creation process.

       Allows the user to:
       - Select products by number
       - Specify purchase quantities
       - Add multiple products to an order
       - Calculate the total payment amount

       Args:
           store_items (store.Store): Store instance used for ordering.

       Prints:
           Order status messages, validation errors,
           and final payment amount.
    """
    all_products = store_items.get_all_products()
    list_of_products_in_store(store_items)
    print("When you want to finish order, enter empty text. ")
    purchased = []
    total_amount = 0
    while True:
        shopping = input("Which product # do you want? ")
        if shopping == "":
            print("Thank You. Welcome!")
            break

        purchase_quantity = input("What amount do you want? ")
        if purchase_quantity == "":
            print("Error while making order!")
            continue

        try:
            shopping = int(shopping)
            purchase_quantity = int(purchase_quantity)

        except ValueError:
            print("Error adding product!")
            continue

        for nos, item in enumerate(all_products, 1):
            if shopping == nos:
                if purchase_quantity <= Product.get_quantity(item):
                    purchased.append((item, int(purchase_quantity)))
                elif purchase_quantity > Product.get_quantity(item):
                    print(
                        "Error while making order! Quantity larger than what "
                        "exists")
        if purchased:
            total_amount += store_items.order(purchased)
            print("Product added to list!")

    if total_amount > 0:
        print("*********")
        print(f"Order made! Total payment: ${total_amount}")


def exit_program():
    """Exit the store application."""
    print("GoodBye!")


def start(store_items):
    """Run the interactive store menu loop.

        Displays menu options and handles user input until
        the user chooses to quit.

        Args:
            store_items (store.Store): Store instance used by the application.
    """
    while True:
        print("\n\tStore Menu")
        print("\t__________")
        print("1. List all products in store\n"
              "2. Show total amount in store\n"
              "3. Make an order\n"
              "4. Quit")

        options = {
            1: list_of_products_in_store,
            2: total_stock_quantity,
            3: make_order
        }

        user_input = input("Please choose a number: ")
        if not user_input.isdigit():
            print("Please provide a valid number")
            continue

        user_input = int(user_input)

        if user_input == 4:
            exit_program()
            break

        action = options.get(user_input)

        if action:
            action(store_items)
        else:
            print("Invalid option")


def main():
    """
        Entry point for the store application.

        Creates sample products, initializes the store,
        and starts the CLI.
    """
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250)
    ]
    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
