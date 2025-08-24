class Category:
    """
    Класс для представления категории товаров в интернет-магазине.
    """

    # Атрибуты класса
    total_categories = 0
    total_products = 0

    def __init__(
            self,
            name: str,
            description: str,
            products: list
    ):
        """
        Конструктор класса Category.

        Args:
            name (str): Название категории.
            description (str): Описание категории.
            products (list): Список товаров (объектов класса Product) в этой категории.
        """
        self.name = name
        self.description = description
        self.products = products

        # Обновляем атрибуты класса
        Category.total_categories += 1
        Category.total_products += len(products)


class Product:
    """
    Класс для представления товара в интернет-магазине.
    """

    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int
    ):
        """
        Конструктор класса Product.

        Args:
            name (str): Название товара.
            description (str): Описание товара.
            price (float): Цена товара.
            quantity (int): Количество товара на складе.
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

