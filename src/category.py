from src.products import Product


class Category:
    name: str
    description: str
    __products: list
    _category_count = 0
    _product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products

        Category._category_count += 1

    def __str__(self):
        total_quantity = 0
        for product in self.__products:
            total_quantity += product.quantity
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product):
        if isinstance(product, Product):
            try:
                self.__products.append(product)
                if product.quantity == 0:
                    raise ValueError("Товар с нулевым количеством не может быть добавлен")
                else:
                    Category._product_count += 1
            finally:
                print("Обработка добавления товара завершена")
        else:
            raise TypeError("Добавлять можно только объекты класса Product")

    @property
    def products(self):
        """Геттер, который будет выводить список товаров в виде строк в формате:
        Название продукта, 80 руб. Остаток: 15 шт."""
        formatted_list = []
        for product in self.__products:
            formatted_list.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return formatted_list

    def middle_price_counter(self):
        """Метод, который подсчитывает средний ценник всех товаров"""
        quantity_sum = 0
        price_sum = 0
        for product in self.__products:
            price_sum += product.price * product.quantity
            quantity_sum += product.quantity
        try:
            return round(price_sum / quantity_sum, 2)
        except ZeroDivisionError:
            return 0
