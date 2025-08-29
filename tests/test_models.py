import pytest

from src.models import Category, LawnGrass, Product, Smartphone


def test_product_creation():
    """Тест создания продукта."""
    product = Product("Test", "Test desc", 100.0, 10)
    assert product.name == "Test"
    assert product.description == "Test desc"
    assert product.price == 100.0
    assert product.quantity == 10


def test_category_creation():
    """Тест создания категории."""
    product = Product("Test", "Test desc", 100.0, 10)
    category = Category("Test Category", "Test desc", [product])

    assert category.name == "Test Category"
    assert len(category.products) == 1
    assert "100.0 руб." in category.products[0]


def test_add_product():
    """Тест добавления продукта в категорию."""
    product1 = Product("Product1", "Desc1", 100.0, 5)
    product2 = Product("Product2", "Desc2", 200.0, 3)

    category = Category("Test", "Test", [product1])
    initial_count = Category.total_products

    category.add_product(product2)

    assert len(category.products) == 2
    assert Category.total_products == initial_count + 1


def test_add_invalid_product():
    """Тест добавления невалидного продукта."""
    product = Product("Valid", "Desc", 100.0, 5)
    category = Category("Test", "Test", [product])

    with pytest.raises(TypeError):
        category.add_product("invalid product")

    with pytest.raises(TypeError):
        category.add_product(123)


def test_price_validation():
    """Тест валидации цены."""
    product = Product("Test", "Test", 100.0, 10)

    # Попытка установить отрицательную цену
    product.price = -50
    assert product.price == 100.0  # Цена не должна измениться

    # Попытка установить нулевую цену
    product.price = 0
    assert product.price == 100.0  # Цена не должна измениться


def test_new_product_method():
    """Тест класса-метода new_product."""
    product_data = {
        "name": "New Product",
        "description": "New desc",
        "price": 150.0,
        "quantity": 7
    }

    product = Product.new_product(product_data)
    assert product.name == "New Product"
    assert product.price == 150.0
    assert product.quantity == 7


def test_duplicate_product_handling():
    """Тест обработки дубликатов продуктов."""
    product1 = Product("Same Name", "Desc1", 100.0, 5)
    products_list = [product1]

    product_data = {
        "name": "Same Name",
        "description": "Different desc",
        "price": 150.0,
        "quantity": 3
    }

    # Должен вернуть существующий продукт с обновленными значениями
    result = Product.new_product(product_data, products_list)
    assert result == product1
    assert result.quantity == 8  # 5 + 3
    assert result.price == 150.0  # Более высокая цена


def test_products_property():
    """Тест геттера products."""
    product1 = Product("Product1", "Desc1", 100.0, 5)
    product2 = Product("Product2", "Desc2", 200.0, 3)

    category = Category("Test", "Test", [product1, product2])

    products_list = category.products

    assert len(products_list) == 2
    assert "100.0 руб." in products_list[0]
    assert "200.0 руб." in products_list[1]


# НОВЫЕ ТЕСТЫ ДЛЯ ДОМАШНЕГО ЗАДАНИЯ
def test_product_str_method():
    """Тест строкового представления продукта."""
    product = Product("Test Product", "Description", 150.0, 8)
    expected = "Test Product, 150.0 руб. Остаток: 8 шт."
    assert str(product) == expected


def test_category_str_method():
    """Тест строкового представления категории."""
    product1 = Product("Prod1", "Desc1", 100.0, 3)
    product2 = Product("Prod2", "Desc2", 200.0, 2)
    category = Category("Test Category", "Description", [product1, product2])

    expected = "Test Category, количество продуктов: 5 шт."
    assert str(category) == expected


def test_category_str_empty():
    """Тест строкового представления пустой категории."""
    category = Category("Empty Category", "Description", [])
    expected = "Empty Category, количество продуктов: 0 шт."
    assert str(category) == expected


def test_product_addition():
    """Тест сложения продуктов."""
    product1 = Product("A", "Desc", 100.0, 2)
    product2 = Product("B", "Desc", 200.0, 3)

    result = product1 + product2
    expected = 100.0 * 2 + 200.0 * 3  # 200 + 600 = 800
    assert result == expected


def test_product_addition_same_product():
    """Тест сложения продукта с самим собой."""
    product = Product("Test", "Desc", 50.0, 4)
    result = product + product
    expected = 50.0 * 4 * 2  # 200 * 2 = 400
    assert result == expected


def test_product_addition_zero_quantity():
    """Тест сложения продуктов с нулевым количеством."""
    product1 = Product("A", "Desc", 100.0, 0)
    product2 = Product("B", "Desc", 200.0, 5)

    result = product1 + product2
    expected = 100.0 * 0 + 200.0 * 5  # 0 + 1000 = 1000
    assert result == expected


def test_product_addition_invalid_type():
    """Тест сложения с неверным типом."""
    product = Product("Test", "Desc", 100.0, 2)

    with pytest.raises(
        TypeError,
        match="Можно складывать только объекты класса Product"
    ):
        product + "invalid_string"

    with pytest.raises(TypeError):
        product + 123


def test_products_property_after_str():
    """Тест что свойство products работает с новым __str__."""
    product = Product("Test", "Desc", 150.0, 5)
    category = Category("Test", "Desc", [product])

    products_list = category.products
    assert len(products_list) == 1
    assert "Test, 150.0 руб. Остаток: 5 шт." in products_list[0]


def test_old_functionality_still_works():
    """Тест что старая функциональность не сломалась."""
    # Создание продуктов
    product = Product("Old", "Desc", 100.0, 10)
    assert product.name == "Old"
    assert product.price == 100.0

    # Создание категории
    category = Category("Old Cat", "Desc", [product])
    assert category.name == "Old Cat"
    assert len(category.products) == 1

    # Добавление продукта
    new_product = Product("New", "Desc", 200.0, 5)
    category.add_product(new_product)
    assert len(category.products) == 2


def test_price_setter_still_works():
    """Тест что сеттер цены все еще работает."""
    product = Product("Test", "Desc", 100.0, 5)

    # Установка валидной цены
    product.price = 150.0
    assert product.price == 150.0

    # Попытка установки невалидной цены
    original_price = product.price
    product.price = -50.0
    assert product.price == original_price  # Цена не изменилась


def test_class_method_still_works():
    """Тест что класс-метод new_product все еще работает."""
    product_data = {
        'name': 'New Method Product',
        'description': 'New desc',
        'price': 300.0,
        'quantity': 8
    }

    product = Product.new_product(product_data)
    assert product.name == 'New Method Product'
    assert product.price == 300.0
    assert product.quantity == 8


# ТЕСТЫ ДЛЯ НОВЫХ КЛАССОВ-НАСЛЕДНИКОВ
def test_smartphone_creation():
    """Тест создания смартфона."""
    smartphone = Smartphone(
        "iPhone 15", "Новый iPhone", 150000.0, 5,
        95.5, "15 Pro", 256, "Space Gray"
    )
    assert smartphone.name == "iPhone 15"
    assert smartphone.description == "Новый iPhone"
    assert smartphone.price == 150000.0
    assert smartphone.quantity == 5
    assert smartphone.efficiency == 95.5
    assert smartphone.model == "15 Pro"
    assert smartphone.memory == 256
    assert smartphone.color == "Space Gray"


def test_lawn_grass_creation():
    """Тест создания газонной травы."""
    grass = LawnGrass(
        "Газонная трава", "Элитная трава", 500.0, 20,
        "Россия", "7 дней", "Зеленый"
    )
    assert grass.name == "Газонная трава"
    assert grass.description == "Элитная трава"
    assert grass.price == 500.0
    assert grass.quantity == 20
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"


def test_smartphone_inheritance():
    """Тест что смартфон наследуется от Product."""
    smartphone = Smartphone(
        "Test", "Desc", 100.0, 1, 90.0, "M1", 128, "Black"
    )
    assert isinstance(smartphone, Product)
    assert issubclass(Smartphone, Product)


def test_lawn_grass_inheritance():
    """Тест что газонная трава наследуется от Product."""
    grass = LawnGrass("Test", "Desc", 100.0, 1, "RU", "7d", "Green")
    assert isinstance(grass, Product)
    assert issubclass(LawnGrass, Product)


# ТЕСТЫ ДЛЯ ОГРАНИЧЕНИЙ СЛОЖЕНИЯ
def test_same_class_addition():
    """Тест сложения товаров одного класса."""
    smartphone1 = Smartphone(
        "Phone1", "Desc1", 100000.0, 2, 90.0, "M1", 128, "Black"
    )
    smartphone2 = Smartphone(
        "Phone2", "Desc2", 80000.0, 3, 85.0, "M2", 64, "White"
    )

    total = smartphone1 + smartphone2
    expected = (100000.0 * 2) + (80000.0 * 3)
    assert total == expected


def test_different_class_addition():
    """Тест попытки сложения товаров разных классов."""
    smartphone = Smartphone(
        "Phone", "Desc", 100000.0, 2, 90.0, "M1", 128, "Black"
    )
    grass = LawnGrass("Grass", "Desc", 500.0, 10, "Russia", "7d", "Green")

    with pytest.raises(
        TypeError,
        match="Нельзя складывать товары разных классов"
    ):
        smartphone + grass


def test_product_and_smartphone_addition():
    """Тест сложения базового продукта и смартфона."""
    product = Product("Product", "Desc", 100.0, 5)
    smartphone = Smartphone(
        "Phone", "Desc", 100000.0, 2, 90.0, "M1", 128, "Black"
    )

    with pytest.raises(
        TypeError,
        match="Нельзя складывать товары разных классов"
    ):
        product + smartphone


def test_product_and_lawn_grass_addition():
    """Тест сложения базового продукта и газонной травы."""
    product = Product("Product", "Desc", 100.0, 5)
    grass = LawnGrass("Grass", "Desc", 500.0, 10, "Russia", "7d", "Green")

    with pytest.raises(
        TypeError,
        match="Нельзя складывать товары разных классов"
    ):
        product + grass


# ТЕСТЫ ДЛЯ ОГРАНИЧЕНИЙ ДОБАВЛЕНИЯ ПРОДУКТОВ
def test_add_smartphone_to_category():
    """Тест добавления смартфона в категорию."""
    category = Category("Смартфоны", "Техника")
    smartphone = Smartphone(
        "Phone", "Desc", 100000.0, 2, 90.0, "M1", 128, "Black"
    )

    category.add_product(smartphone)
    assert len(category.products) == 1
    assert isinstance(category.products_objects[0], Smartphone)


def test_add_lawn_grass_to_category():
    """Тест добавления газонной травы в категорию."""
    category = Category("Сад", "Растения")
    grass = LawnGrass("Grass", "Desc", 500.0, 10, "Russia", "7d", "Green")

    category.add_product(grass)
    assert len(category.products) == 1
    assert isinstance(category.products_objects[0], LawnGrass)


def test_add_invalid_object_to_category():
    """Тест попытки добавления невалидного объекта в категорию."""
    category = Category("Тест", "Описание")

    with pytest.raises(
        TypeError,
        match="Можно добавлять только объекты класса Product"
    ):
        category.add_product("не продукт")

    with pytest.raises(TypeError):
        category.add_product(123)

    with pytest.raises(TypeError):
        category.add_product([])


def test_add_valid_subclasses_to_category():
    """Тест добавления всех валидных подклассов Product."""
    category = Category("Разное", "Разные товары")

    product = Product("Product", "Desc", 100.0, 5)
    smartphone = Smartphone(
        "Phone", "Desc", 100000.0, 2, 90.0, "M1", 128, "Black"
    )
    grass = LawnGrass("Grass", "Desc", 500.0, 10, "Russia", "7d", "Green")

    category.add_product(product)
    category.add_product(smartphone)
    category.add_product(grass)

    assert len(category.products) == 3
    assert isinstance(category.products_objects[0], Product)
    assert isinstance(category.products_objects[1], Smartphone)
    assert isinstance(category.products_objects[2], LawnGrass)


# ТЕСТЫ ДЛЯ СТАТИСТИКИ КАТЕГОРИЙ
def test_category_statistics():
    """Тест статистики категорий и продуктов."""
    # Сбросим счетчики для чистого теста
    Category.total_categories = 0
    Category.total_products = 0

    product1 = Product("Prod1", "Desc", 100.0, 5)
    product2 = Product("Prod2", "Desc", 200.0, 3)

    category = Category("Cat1", "Desc", [product1, product2])

    assert Category.total_categories == 1
    assert Category.total_products == 2

    product3 = Product("Prod3", "Desc", 300.0, 2)
    category.add_product(product3)

    assert Category.total_products == 3


def test_product_count_property():
    """Тест свойства product_count."""
    product1 = Product("Prod1", "Desc", 100.0, 5)
    product2 = Product("Prod2", "Desc", 200.0, 3)

    category = Category("Test", "Desc", [product1, product2])
    assert category.product_count == 2

    product3 = Product("Prod3", "Desc", 300.0, 2)
    category.add_product(product3)
    assert category.product_count == 3


# ТЕСТЫ ДЛЯ ПРОВЕРКИ СОВМЕСТИМОСТИ
def test_mixed_products_in_category():
    """Тест смешанных продуктов в категории."""
    category = Category("Mixed", "Разные товары")

    regular_product = Product("Regular", "Desc", 100.0, 5)
    smartphone = Smartphone(
        "Smart", "Desc", 100000.0, 2, 90.0, "M1", 128, "Black"
    )
    grass = LawnGrass("Grass", "Desc", 500.0, 10, "Russia", "7d", "Green")

    category.add_product(regular_product)
    category.add_product(smartphone)
    category.add_product(grass)

    assert category.product_count == 3
    assert "Regular, 100.0 руб. Остаток: 5 шт." in category.products
    assert "Smart, 100000.0 руб. Остаток: 2 шт." in category.products
    assert "Grass, 500.0 руб. Остаток: 10 шт." in category.products


def test_category_iterator_with_subclasses():
    """Тест итератора категории с подклассами."""
    category = Category("Test", "Desc")

    smartphone = Smartphone(
        "Phone", "Desc", 100000.0, 2, 90.0, "M1", 128, "Black"
    )
    grass = LawnGrass("Grass", "Desc", 500.0, 10, "Russia", "7d", "Green")

    category.add_product(smartphone)
    category.add_product(grass)

    products = list(category.products_objects)
    assert len(products) == 2
    assert isinstance(products[0], Smartphone)
    assert isinstance(products[1], LawnGrass)

