from src.products import Category, Product


def test_product(samsung: Product):
    assert samsung.name == "Samsung Galaxy S23 Ultra"
    assert samsung.description == "256GB, Серый цвет, 200MP камера"
    assert samsung.price == 180000.0
    assert samsung.quantity == 5


def test_category(phone: Category):
    assert phone.name == "Смартфоны"
    assert (
        phone.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert Category.category_count == 1
    assert Category.product_count == 1
