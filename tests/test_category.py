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
