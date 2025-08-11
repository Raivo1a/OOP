from src.products import Product


class LawnGrass(Product):

    def __init__(
        self,
        name: str,
        description: str,
        country: str,
        germination_period: str,
        color: str,
        __price: float = 0,
        quantity: int = 0,
    ):
        super().__init__(name, description, __price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
