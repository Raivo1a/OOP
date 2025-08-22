from src.products import Product


def test_mixin(capsys):
    Product("Apple Iphone 16", "512GB", 95.5, 16)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Product (Apple Iphone 16, 512GB, 95.5, 16)"
