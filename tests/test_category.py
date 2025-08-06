from src.category import Category


def test_category(phone: Category):
    assert phone.name == "Смартфоны"
    assert (
        phone.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert Category.category_count == 1
    assert Category.product_count == 0
