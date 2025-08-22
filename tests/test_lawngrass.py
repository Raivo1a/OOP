from src.lawngrass import LawnGrass


def test_lawngrass(grass: LawnGrass):
    assert grass.name == "Газонная трава"
    assert grass.description == "Универсальная"
    assert grass.country == "США"
    assert grass.germination_period == "5 дней"
    assert grass.color == "Темно-зеленый"
    assert grass.price == 500
    assert grass.quantity == 10
