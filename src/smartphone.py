from src.products import Product


class Smartphone(Product):

    def __init__(
        self,
        name: str,
        description: str,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
        __price: float = 0,
        quantity: int = 0,
    ):
        super().__init__(name, description, __price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
