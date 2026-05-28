import pytest

from products import Product, LimitedProduct
from promotions import Promotion


def test_creating_prod():
    """ Verify that a Product instance is created successfully with valid
    initialization parameters. """
    product1 = Product("Mac Book", 1000, 500)
    assert product1.name == "Mac Book"


def test_creating_invalid_details():
    """ Verify that invalid product initialization values raise ValueError
    exceptions. """
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)
        Product("MacBook Air M2", price=-10, quantity=100)


def test_prod_becomes_inactive():
    """ Verify that a product is automatically deactivated when initialized
    with zero quantity. """
    product1 = Product("Mac Book", 1000, 0)
    assert product1.is_active() == False


def test_buy_modifies_quantity():
    """ Verify that purchasing a product reduces the available inventory
    quantity and returns the correct total price. """
    product1 = Product("Mac Book", 1000, 500)
    assert product1.buy(300) == 300000


def test_buy_too_much():
    """ Verify that attempting to purchase more items than available in
    stock raises a ValueError. """
    product1 = Product("Mac Book", 1000, 500)
    with pytest.raises(ValueError):
        product1.buy(600)


def test_ordering_limit():
    """ Verify that a LimitedProduct prevents purchases exceeding the
    configured maximum order quantity. """
    product1 = LimitedProduct("Mac Book", 1000, 250, 3)
    with pytest.raises(ValueError):
        product1.buy(500)


def test_promotion():
    """ Verify that assigning an invalid promotion raises a ValueError. """
    product1 = LimitedProduct("Mac Book", 1000, 250, 3)
    with pytest.raises(ValueError):
        product1.set_promotion(None)


pytest.main()
