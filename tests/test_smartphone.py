from src.smartphone import Smartphone


def test_smartphone(samsung: Smartphone):
    assert samsung.name == "Samsung Galaxy S23 Ultra"
    assert samsung.description == "256GB, Серый цвет, 200MP камера"
    assert samsung.efficiency == 95.5
    assert samsung.model == "S23 Ultra"
    assert samsung.memory == 256
    assert samsung.color == "Серый"
    assert samsung.price == 180000.0
    assert samsung.quantity == 5
