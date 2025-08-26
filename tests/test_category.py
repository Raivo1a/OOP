import pytest

from src.category import Category
from src.products import Product


def test_category(phone: Category):
    assert phone.name == "Смартфоны"
    assert (
        phone.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert Category._category_count == 1


def test_str_category(phone: Category):
    assert str(phone) == "Смартфоны, количество продуктов: 10 шт."


def test_add_product(sample_category):
    invalid_item = "Не продукт"
    with pytest.raises(TypeError, match="Добавлять можно только объекты класса Product"):
        sample_category.add_product(invalid_item)
    assert len(sample_category.products) == 0
    assert Category._product_count == 0


def test_add_product_value_error(sample_category):
    zero_quantity = Product("Xiaomi Mi 13", "256GB", 70000.0, 0)
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        sample_category.add_product(zero_quantity)


def test_middle_price_counter(phone: Category):
    assert phone.middle_price_counter() == 165000.00


def test_middle_price_counter_zero_quantity():
    empty_category = Category("Пусто", "Без продуктов", [])
    assert empty_category.middle_price_counter() == 0
