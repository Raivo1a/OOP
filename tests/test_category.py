import pytest

from src.category import Category


def test_category(phone: Category):
    assert phone.name == "Смартфоны"
    assert (
        phone.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert Category._category_count == 1


def test_str_category(phone: Category):
    assert str(phone) == "Смартфоны, количество продуктов: 10 шт."


@pytest.fixture
def sample_category():
    Category._category_count = 0
    Category._product_count = 0
    return Category("Тестовая категория", "Для тестов type error", [])


def test_add_product(sample_category):
    invalid_item = "Не продукт"
    with pytest.raises(TypeError, match="Добавлять можно только объекты класса Product"):
        sample_category.add_product(invalid_item)
    assert len(sample_category.products) == 0
    assert Category._product_count == 0
