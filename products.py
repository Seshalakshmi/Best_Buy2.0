from typing import Union
from promotions import Promotion

class Product:
    """
        Represents a product with a name, price, quantity, and active status.

        Provides methods to get and set attributes, activate/deactivate the
        product,
        display product information, and process purchases.
    """

    def __init__(self, name: str, price:Union[float, int], quantity: int):
        """
        Initialize a Product instance.

        Args:
            name: Product name.
            price: Unit price of the product.
            quantity: Initial stock quantity.

        Raises:
            TypeError: If any argument has an invalid type.
            ValueError: If name is empty, or if price/quantity are negative.
        """
        if not isinstance(name, str):
            raise TypeError("Name should be string")

        if not isinstance(price, (float, int)):
            raise TypeError("Price should be a float or integer")

        if not isinstance(quantity, int):
            raise TypeError("Quantity should be an integer")

        if not name:
            raise ValueError("Name is required")

        if price is None or price < 0:
            raise ValueError("Price is required")

        if quantity is None or quantity < 0:
            raise ValueError("Quantity is required")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

        if self.quantity == 0:
            self.deactivate()

        self.promotion = None

    def set_promotion(self, promotion: Promotion):
        """
        Assign a promotion to the product.

        Args: promotion (Promotion): Promotion instance to apply.
        Raises: ValueError: If the provided promotion is invalid.

        """
        if promotion:
            self.promotion = promotion
        else:
            raise ValueError("Promotion is invalid")

    def get_promotion(self):
        """
        Retrieve the currently assigned promotion.

        Returns: Promotion | None: Assigned promotion instance, if any.
        """
        return self.promotion

    def get_quantity(self) -> int:
        """Return the available quantity of the product."""
        return self.quantity

    def set_quantity(self, new_quantity: int):
        """
                Set a new quantity for the product.

                Args:
                    new_quantity (int): The updated stock quantity (must be
                    positive).

                Raises:
                    ValueError: If quantity is not a positive integer.
                    TypeError: If type is invalid.
        """
        if not isinstance(new_quantity, int) and new_quantity > 0:
            raise TypeError("Quantity is Invalid")

        if new_quantity > self.quantity:
            raise ValueError("Quantity is out of stock")

        if new_quantity < 0:
            raise ValueError("Please type a positive number")

        self.quantity -= new_quantity

        if self.quantity == 0:
            self.deactivate()
        else:
            self.activate()

    def is_active(self) -> bool:
        """
            Check whether the product is active.

            Returns:
                bool: True if active, False otherwise.
        """
        return self.active

    def activate(self):
        """
            Activate the product.

            Returns:
                bool: True after activation.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivate the product.

        Returns:
            bool: False after deactivation.
        """
        self.active = False

    def show(self):
        """
        Generate a formatted representation of the product.
        Returns: str: Human-readable product description including pricing,
        quantity, and promotion details.
        """
        if self.promotion:
            return (f"{self.name}, Price: {self.price}, Quantity: "
                    f"{self.quantity}, Promotion: {self.promotion.name}")

        return (f"{self.name}, Price: {self.price}, Quantity: "
                f"{self.quantity}, Promotion: None")

    def buy(self, quantity: int) -> float:
        """
        Purchase a specified quantity of the product.
        Reduces available stock and applies any assigned promotion.

        Args: quantity (int): Number of units to purchase.
        Returns: float: Total purchase cost.

        Raises: ValueError: If the product is inactive, quantity is invalid,
        or insufficient stock is available.
        """
        if not self.active:
            raise ValueError("This product is inactive")

        if self.promotion:
            total_price = self.promotion.apply_promotion(self.price, quantity)
        else:
            total_price = self.price * quantity

        self.set_quantity(quantity)

        return float(total_price)


class NonStockedProduct(Product):
    """
    Represents a product with unlimited availability.
    Unlike standard products, non-stocked products are never depleted
    and remain active indefinitely.
    """

    def __init__(self, name: str, price: float):
        """
        Initialize a NonStockedProduct instance.
        Args: name (str): Product name. price (float): Unit price of the
        product.
        """
        super().__init__(name, price, quantity=0)
        self.activate()

    def show(self) -> str:
        """ Generate a formatted representation of the non-stocked product.
        Returns: str: Product description including unlimited availability. """
        if self.promotion:
            return (f"{self.name}, Price: {self.price}, "
                    f"Quantity: Unlimited, Promotion: {self.promotion.name}")
        return (f"{self.name}, Price: {self.price}, "
                f"Quantity: Unlimited, Promotion: None")

    def buy(self, quantity: int):
        """
        Purchase a specified quantity of the product.
        Since stock is unlimited, inventory is not reduced.

        Args: quantity (int): Number of units to purchase.

        Returns: float: Total purchase cost.

        Raises: ValueError: If the product is inactive or quantity is invalid.
        """
        if not self.active:
            raise ValueError("This product is inactive")
        if quantity <= 0:
            raise ValueError("Purchase Quantity must be positive")

        if self.promotion:
            total_price = self.promotion.apply_promotion(self.price, quantity)
        else:
            total_price = self.price * quantity

        return float(total_price)


class LimitedProduct(Product):
    """
    Represents a product with a purchase limit per order.
    Customers may only purchase up to a specified maximum quantity
    in a single transaction.
    """

    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        """ 
        Initialize a LimitedProduct instance. 
        
        Args: 
            name (str): Product name. 
            price (float): Unit price of the product. 
            quantity (int): Available inventory quantity. 
            maximum (int): Maximum quantity allowed per order. 
        
        Raises: ValueError: If maximum is less than or equal to zero. 
        """
        if maximum <= 0:
            raise ValueError("Maximum limit must be greater than 0")

        self.maximum = maximum


    def show(self) -> str:
        """
        Generate a formatted representation of the limited product.
        Returns: str: Product description including purchase limitation.
        """
        if self.promotion:
            return (f"{self.name}, Price: {self.price}, "
                    f"Quantity: Limited to {self.maximum} per order!, "
                    f"Promotion: {self.promotion}")
        return (f"{self.name}, Price: {self.price}, "
                f"Quantity: Limited to {self.maximum} per order!, Promotion: "
                f"None")

    def buy(self, quantity: int) -> float:
        """
        Purchase a specified quantity of the product.
        Ensures the requested quantity does not exceed the allowed per-order
        purchase limit.

         Args:quantity (int): Number of units to purchase.

        Returns: float: Total purchase cost.

        Raises: ValueError: If the requested quantity exceeds the allowed
        limit.
        """
        if quantity > self.maximum:
            raise ValueError(
                f"Cannot purchase more than {self.maximum} items at once")

        return quantity * self.promotion
