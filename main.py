import store
from products import Product, NonStockedProduct, LimitedProduct
from promotions import PercentDiscount, SecondHalfPrice, ThirdOneFree


def list_of_products_in_store(store_items):
    """Display all available products in the store.

        Args:
            store_items (store.Store): Store instance containing products.

        Prints:
            Enumerated list of products with details.
    """
    all_products = store_items.get_all_products()
    for nos, item in enumerate(all_products, 1):
        print(f"{nos}: {item.show()}")

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
            shopping = int(shopping) - 1
            purchase_quantity = int(purchase_quantity)

        except ValueError:
            print("Error adding product!")
            continue

        if shopping < 0 or shopping >= len(all_products):
            print("Error: Invalid product number!")
            continue

        item = all_products[shopping]

        current_stock = item.get_quantity()

        if isinstance(item,
                      LimitedProduct) and purchase_quantity > item.maximum:
            print(
                f"Error while making order! Quantity larger than maximum "
                f"allowed per order ({item.maximum})")
            continue

            # Check stock limits (ignore check for NonStockedProduct since
            # it has unlimited stock)
        if (not isinstance(item,
                          NonStockedProduct) and purchase_quantity >
                current_stock):
            print("Error while making order! Quantity larger than what exists")
            continue

        if purchase_quantity <= 0:
            print("Error: Quantity must be greater than zero.")
            continue

        purchased.append((item, purchase_quantity))
        print("Product added to list!")

    if purchased:
        try:
            total_payment = store_items.order(purchased)
            print("*********")
            print(f"Order made! Total payment: ${total_payment:.2f}")
        except Exception as e:
            print(f"Order execution failed: {e}")
    else:
        print("No items ordered.")


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
    # setup initial stock of inventory
    # setup initial stock of inventory
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        NonStockedProduct("Windows License", price=125),
        LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    ]

    # Create promotion catalog
    second_half_price = SecondHalfPrice("Second Half price!")
    third_one_free = ThirdOneFree("Third One Free!")
    thirty_percent = PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
