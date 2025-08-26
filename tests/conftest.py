import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.smartphone import Smartphone


@pytest.fixture()
def samsung() -> Smartphone:
    return Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        95.5,
        "S23 Ultra",
        256,
        "Серый",
        180000.0,
        5,
    )


@pytest.fixture()
def phone(samsung, apple) -> Category:
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        [samsung, apple],
    )


@pytest.fixture()
def apple() -> Smartphone:
    return Smartphone("Apple Iphone 16", "512GB", 95.5, "16", 512, "Белый", 150000, 5)


@pytest.fixture()
def grass() -> LawnGrass:
    return LawnGrass("Газонная трава", "Универсальная", "США", "5 дней", "Темно-зеленый", 500, 10)


@pytest.fixture
def sample_category():
    Category._category_count = 0
    Category._product_count = 0
    return Category("Тестовая категория", "Для тестов", [])
