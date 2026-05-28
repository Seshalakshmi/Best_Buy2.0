class Product:
    """
        Represents a product with a name, price, quantity, and active status.

        Provides methods to get and set attributes, activate/deactivate the product,
        display product information, and process purchases.
    """
    def __init__(self, name:str, price:float, quantity:int):
        """
                Initialize a new Product instance.

                Args:
                    name (str): The name of the product.
                    price (int | float): The price per unit of the product.
                    quantity (int): The available stock quantity.
        """
        if not name:
            raise ValueError("Name is required")

        if price is None or price < 0:
            raise ValueError("Price is required")

        if quantity is None or quantity < 0:
            raise ValueError("Quantity is required")

        try:
            self._name = name
            self._price = price
            self._quantity = quantity

            if self._quantity == 0:
                self.deactivate()
            else:
                self.activate()

        except ValueError as e:
            print(e)



    def get_quantity(self) -> int:
        """Return the available quantity of the product."""
        return self._quantity

    def set_quantity(self, new_quantity):
        """
                Set a new quantity for the product.

                Args:
                    new_quantity (int): The updated stock quantity (must be positive).

                Raises:
                    ValueError: If quantity is not a positive integer.
                    TypeError: If type is invalid.
        """
        try:
            if isinstance(new_quantity, int) and new_quantity > 0:
                self._quantity = new_quantity
            else:
                raise ValueError("New Quantity is Invalid")
        except TypeError:
            print("Quantity should be a integer")
        except ValueError as e:
            print(e)

    def is_active(self):
        """
            Check whether the product is active.

            Returns:
                bool: True if active, False otherwise.
        """
        return self._active

    def activate(self):
        """
            Activate the product.

            Returns:
                bool: True after activation.
        """
        self._active = True


    def deactivate(self):
        """
        Deactivate the product.

        Returns:
            bool: False after deactivation.
        """
        self._active = False


    def show(self):
        """
                Return a formatted string describing the product.

                Returns:
                    str: Product details.
        """
        return (f"{self._name}, Price: {self._price}, Quantity: "
                f"{self._quantity}")

    def buy(self, quantity):
        """
            Purchase a given quantity of the product.

            Reduces stock if enough quantity is available.

            Args:
                quantity (int): Number of items to purchase.

            Returns:
                float: Total price for the purchase.
                None: If purchase is invalid or insufficient stock.
        """
        if self._active:
            if quantity > self._quantity:
                raise ValueError("Quantity is out of stock")
            if quantity <= 0:
                raise ValueError("Please type a positive number")

            self._quantity -= quantity

            if self._quantity == 0:
                self.deactivate()
            return float(self._price * quantity)
        else:
            raise ValueError("This product is inactive")
