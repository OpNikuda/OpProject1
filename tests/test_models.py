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