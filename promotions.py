from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, price, quantity: int) -> float:
        pass


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, price, quantity: int) -> float:
        total = quantity * price
        percent = total * self.percent / 100
        return total - percent


class SecondHalfPrice(Promotion):
    def apply_promotion(self, price, quantity: int) -> float:
        pairs = quantity // 2
        left_over = quantity % 2
        pair_price = pairs * (price + (price / 2))
        left_over_price = price * left_over
        return pair_price + left_over_price


class ThirdOneFree(Promotion):
    def apply_promotion(self, price, quantity: int) -> float:
        group_of_3 = quantity // 3
        left_over = quantity % 3
        paid_items = (group_of_3 * 2) + left_over
        return paid_items * price
