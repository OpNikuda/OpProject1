import pytest
from src.models import Product, Category


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
    product1 = Product(
        "Product1",
        "Desc1",
        100.0,
        5
    )

    product2 = Product(
        "Product2",
        "Desc2",
        200.0,
        3
    )

    category = Category(
        "Test",
        "Test",
        [product1, product2]
    )

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