from base_product import BaseProduct
from mixin import Mixin


class Product(BaseProduct, Mixin):
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, __price: float = 0, quantity: int = 0):
        if __price < 0:
            raise ValueError("Цена не может быть отрицательной")
        if quantity < 0:
            raise ValueError("Кол-во не может быть отрицательным")

        self.name = name
        self.description = description
        self.__price = __price
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    @classmethod
    def new_product(cls, product_data, existing_products):
        """Принимает на вход параметры товара в словаре и возвращает созданный объект класса Product"""
        name = product_data.get("name") or ""
        description = product_data.get("description") or ""
        price = product_data.get("price", 0.0)
        quantity = product_data.get("quantity", 0)

        if existing_products:
            for product in existing_products:
                if product.name == name:
                    product.quantity += quantity
                    product.price = max(product.price, price)
                    return product
        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        """Геттер возвращает значение приватного атрибута цены"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер делает проверку на положительное значение новой цены"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        if new_price < self.__price:
            confirm = input(f"Вы уверены, что хотите понизить цену с {self.__price} до {new_price}? (y/n): ")
            if confirm.lower() == "y":
                self.__price = new_price
                print(f"Цена понижена до {new_price}")
            else:
                print("Понижение цены отменено")
        else:
            self.__price = new_price

    def __add__(self, other):
        if type(other) is self.__class__:
            return (self.__price * self.quantity) + (other.__price * other.quantity)
        else:
            raise TypeError
