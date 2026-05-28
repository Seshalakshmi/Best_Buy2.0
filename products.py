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

        self._name = name
        self._price = price
        self._quantity = quantity
        self._active = True

        if self._quantity == 0:
            self.deactivate()



    def get_quantity(self) -> int:
        """Return the available quantity of the product."""
        return self._quantity

    def set_quantity(self, new_quantity: int):
        """
                Set a new quantity for the product.

                Args:
                    new_quantity (int): The updated stock quantity (must be positive).

                Raises:
                    ValueError: If quantity is not a positive integer.
                    TypeError: If type is invalid.
        """
        if not isinstance(new_quantity, int) and new_quantity < 0:
            raise ValueError("Quantity should be a integer")
        self._quantity = new_quantity
        if self._quantity == 0:
            self.deactivate()
        else:
            self.activate()


    def is_active(self) -> bool:
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

    def buy(self, quantity: int) -> float:
        """
            Purchase a given quantity of the product.

            Reduces stock if enough quantity is available.

            Args:
                quantity (int): Number of items to purchase.

            Returns:
                float: Total price for the purchase.
                None: If purchase is invalid or insufficient stock.
        """
        if not self._active:
            raise ValueError("This product is inactive")
        if quantity > self._quantity:
            raise ValueError("Quantity is out of stock")
        if quantity <= 0:
            raise ValueError("Purchase Quantity must be positive")

        self._quantity -= quantity

        if self._quantity == 0:
            self.deactivate()
        return float(self._price * quantity)



class NonStockedProduct(Product):
    def __init__(self, name:str, price:float):
        super().__init__(name, price, quantity=0)
        self.activate()

    def show(self) -> str:
        return (f"{self._name}, Price: {self._price}, "
                f"Quantity: Unlimited, Promotion: 30% off!")

    def buy(self, quantity: int):
        super().buy(quantity)
        
class LimitedProduct(Product):
    def __init__(self, name:str, price:float, quantity:int, maximum:int):
        super().__init__(name, price, quantity)
        if maximum <= 0:
            raise ValueError("Maximum limit must be greater than 0")
        self.maximum = maximum


    def show(self) -> str:
        return (f"{self._name}, Price: {self._price}, "
                f"Quantity: Limited to {self.maximum} per order!, Promotion: None)")

    def buy(self, quantity: int) -> float:
        if quantity > self.maximum:
            raise ValueError(f"Cannot purchase more than {self.maximum} items at once")
        return super().buy(quantity)