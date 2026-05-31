from products import Product

class Store:
    """
    Represents a store that manages a collection of Product objects.

    Provides functionality to add/remove products, calculate total stock,
    retrieve active products, and process customer orders.
    """

    def __init__(self, list_of_products:list[Product]):
        """
        Initialize a Store instance.

        Args:
            list_of_products: Initial collection of products.

        Raises:
            TypeError: If `list_of_products` is not a list.
        """
        if not all(isinstance(item, Product) for item in list_of_products):
            raise TypeError("All items must be Product instances")

        self.list_of_products = list_of_products

    def add_product(self, product: Product):
        """
        Add a product to the store inventory.

        Args:
            product: Product to add.

        Raises:
            TypeError: If `product` is not a Product instance.
        """
        if not isinstance(product, Product):
            raise TypeError("products must be a Product")

        self.list_of_products.append(product)

    def remove_product(self, product):
        """
        Remove a product from the store inventory.

        Args:
            product: Product to remove.

        Raises:
            TypeError: If `product` is not a Product instance.
            ValueError: If the product does not exist in the inventory.
        """
        if not isinstance(product, Product):
            raise TypeError("products must be a Product")

        if product not in self.list_of_products:
            raise ValueError("Product not found")

        self.list_of_products.remove(product)


    def get_total_quantity(self):
        """
        Calculate the total quantity of all products in inventory.

        Returns:
            int: Total number of units available across all products.

        Raises:
            TypeError: If an inventory item is not a Product instance.
        """
        total_quantity = 0

        for item in self.list_of_products:
            if not isinstance(item, Product):
                raise TypeError("Item must be Product")

            total_quantity += item.get_quantity()

        return total_quantity


    def get_all_products(self):
        """
        Retrieve all active products in the store.

        Returns:
            list[Product] | str: List of active products,
            or a message if no active products exist.
        """
        active_products = [item for item in self.list_of_products if
                           item.is_active() == True]

        if not active_products:
            return "There is no product in this store"

        return active_products

    def order(self, shopping_list) -> float:
        """
        Process a customer order.

        Each item in shopping_list should be a tuple:
        (Product, quantity)

        Args:
            shopping_list (list[tuple]): List of (Product, quantity) pairs.

        Returns:
            float: Total price of the order.
        """
        total_price = 0
        for item, quantity in shopping_list:
            total_price += item.buy(quantity)

        return float(total_price)
