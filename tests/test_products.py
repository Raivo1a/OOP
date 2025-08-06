from unittest.mock import patch

import pytest

from src.products import Product


def test_product(samsung: Product):
    assert samsung.name == "Samsung Galaxy S23 Ultra"
    assert samsung.description == "256GB, Серый цвет, 200MP камера"
    assert samsung.price == 180000.0
    assert samsung.quantity == 5


def test_negative_price():
    with pytest.raises(ValueError):
        Product("Test Product", "Description", -100.0, 5)


def test_negative_quantity():
    with pytest.raises(ValueError):
        Product("Test Product", "Description", 100.0, -5)


def test_set_lower_price(samsung: Product):
    with patch("builtins.input", return_value="y"):
        samsung.price = 150000
        assert samsung.price == 150000


def test_set_lower_price_denied(samsung: Product):
    with patch("builtins.input", return_value="n"):
        samsung.price = 150000
        assert samsung.price == 180000


def test_str_product(apple: Product):
    assert str(apple) == "Apple Iphone 16, 150000 руб. Остаток: 5 шт."


def test_add_product(apple: Product, samsung: Product):
    assert apple + samsung == 1650000
