class Product:
    """Класс для представления товара."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
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
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """
        Сложение товаров - возвращает общую стоимость всех товаров.

        Args:
            other (Product): Другой товар для сложения.

        Returns:
            float: Общая стоимость товаров.

        Raises:
            TypeError: Если передан не объект класса Product или классы не совпадают.
        """
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product")

        if type(self) != type(other):
            raise TypeError("Нельзя складывать товары разных классов")

        return (self.price * self.quantity) + (other.price * other.quantity)


class Smartphone(Product):
    """Класс для представления смартфона."""

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str):
        """
        Конструктор класса Smartphone.

        Args:
            name (str): Название смартфона.
            description (str): Описание смартфона.
            price (float): Цена смартфона.
            quantity (int): Количество в наличии.
            efficiency (float): Производительность.
            model (str): Модель смартфона.
            memory (int): Объем встроенной памяти.
            color (str): Цвет смартфона.
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс для представления газонной травы."""

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
        """
        Конструктор класса LawnGrass.

        Args:
            name (str): Название травы.
            description (str): Описание травы.
            price (float): Цена травы.
            quantity (int): Количество в наличии.
            country (str): Страна-производитель.
            germination_period (str): Срок прорастания.
            color (str): Цвет травы.
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category:
    """Класс для представления категории товаров в интернет-магазине."""

    # Атрибуты класса
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str, products: list = None):
        """
        Конструктор класса Category.

        Args:
            name (str): Название категории.
            description (str): Описание категории.
            products (list): Список товаров в этой категории.
        """
        self.name = name
        self.description = description
        self.__products = products if products else []

        # Обновляем атрибуты класса
        Category.total_categories += 1
        Category.total_products += len(self.__products)

    def __str__(self):
        """
        Строковое представление категории.

        Returns:
            str: Строка с информацией о категории и общем количестве товаров.
        """
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

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


class CategoryIterator:
    """Итератор для перебора товаров в категории."""

    def __init__(self, category):
        """
        Конструктор итератора.

        Args:
            category (Category): Объект категории для итерации.
        """
        self.category = category
        self.index = 0

    def __iter__(self):
        """Возвращает сам итератор."""
        return self

    def __next__(self):
        """
        Возвращает следующий товар в категории.

        Returns:
            Product: Следующий товар.

        Raises:
            StopIteration: Когда товары закончились.
        """
        if self.index < len(self.category.products_objects):
            product = self.category.products_objects[self.index]
            self.index += 1
            return product
        raise StopIteration