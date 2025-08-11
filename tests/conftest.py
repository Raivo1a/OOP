import pytest

from src.category import Category
from src.products import Product


@pytest.fixture()
def samsung() -> Product:
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture()
def phone(samsung, apple) -> Category:
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        [samsung, apple],
    )


@pytest.fixture()
def apple() -> Product:
    return Product("Apple Iphone 16", "512GB", 150000, 5)
