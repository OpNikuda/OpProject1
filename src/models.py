class Product:
    """
    Класс для представления товара.
    """

    def __init__(self, name: str, description: str, price: float,
                 quantity: int):
        """
        Конструктор класса Product.

        Args:
            name (str): Название товара.
            description (str): Описание товара.
            price (float): Цена товара.
            quantity (int): Количество товара в наличии.
        """
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict, products_list: list = None):
        """
        Класс-метод для создания нового товара.
        Проверяет наличие товара с таким же именем и объединяет при
        необходимости.

        Args:
            product_data (dict): Словарь с данными товара.
            products_list (list, optional): Список существующих товаров для
                проверки дубликатов.

        Returns:
            Product: Новый или существующий товар.
        """
        name = product_data.get('name')
        description = product_data.get('description')
        price = product_data.get('price')
        quantity = product_data.get('quantity')

        # Проверка на дубликаты
        if products_list:
            for existing_product in products_list:
                if existing_product.name.lower() == name.lower():
                    # Объединяем количества
                    existing_product.quantity += quantity
                    # Выбираем максимальную цену
                    if price > existing_product.price:
                        existing_product.price = price
                    return existing_product

        # Если дубликат не найден, создаем новый товар
        return cls(name, description, price, quantity)

    @property
    def price(self):
        """Геттер для цены."""
        return self.__price

    @price.setter
    def price(self, new_price: float):
        """
        Сеттер для цены с проверкой валидности.

        Args:
            new_price (float): Новая цена товара.

        Raises:
            ValueError: Если цена равна или меньше нуля.
        """
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        # Подтверждение понижения цены
        if new_price < self.__price:
            confirmation = input(
                f"Цена понижается с {self.__price} до {new_price}."
                f" Подтвердите (y/n): "
            )
            if confirmation.lower() != 'y':
                print("Изменение цены отменено")
                return

        self.__price = new_price

    def __str__(self):
        """Строковое представление товара."""
        return (f"{self.name}, {self.price} руб. "
                f"Остаток: {self.quantity} шт.")


class Category:
    """
    Класс для представления категории товаров в интернет-магазине.
    """

    # Атрибуты класса
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str, products: list):
        """
        Конструктор класса Category.

        Args:
            name (str): Название категории.
            description (str): Описание категории.
            products (list): Список товаров в этой категории.
        """
        self.name = name
        self.description = description
        self.__products = products  # Приватный атрибут

        # Обновляем атрибуты класса
        Category.total_categories += 1
        Category.total_products += len(products)

    def add_product(self, product):
        """
        Добавляет товар в категорию.

        Args:
            product: Объект класса Product для добавления.

        Raises:
            TypeError: Если передан не объект класса Product.
        """
        # Проверка типа
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product")

        # Добавление в приватный список
        self.__products.append(product)

        # Обновление счетчика
        Category.total_products += 1

    @property
    def products(self):
        """
        Геттер для списка товаров в виде форматированных строк.

        Returns:
            list: Список строк с информацией о товарах.
        """
        return [str(product) for product in self.__products]

    @property
    def products_objects(self):
        """
        Геттер для получения объектов товаров.

        Returns:
            list: Список объектов товаров.
        """
        return self.__products

    @property
    def product_count(self):
        """
        Геттер для количества товаров в категории.

        Returns:
            int: Количество товаров в категории.
        """
        return len(self.__products)