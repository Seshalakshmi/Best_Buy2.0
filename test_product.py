import pytest

from products import Product

def test_creating_prod():
    product1 = Product("Mac Book", 1000, 500)
    assert product1._name == "Mac Book"

def test_creating_invalid_details():
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)
        Product("MacBook Air M2", price=-10, quantity=100)


def test_prod_becomes_inactive():
    product1 = Product("Mac Book", 1000, 0)
    assert product1.is_active() == False


def test_buy_modifies_quantity():
    product1 = Product("Mac Book", 1000, 500)
    assert product1.buy(300) == 300000


def test_buy_too_much():
    product1 = Product("Mac Book", 1000, 500)
    with pytest.raises(ValueError):
        product1.buy(600)

pytest.main()