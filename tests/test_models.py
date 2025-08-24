from src.models import Product, Category


def test_total_categories_count():
    """Тест подсчета количества категорий."""
    # Сбрасываем счетчики для чистоты теста
    Category.total_categories = 0
    Category.total_products = 0

    assert Category.total_categories == 2
    assert Category.total_products == 0  # В категориях нет продуктов


def test_product_initialization():
    """Тест корректности инициализации объекта Product."""
    product = Product("Тестовый товар", "Описание тестового товара", 100, 5)

    assert product.name == "Тестовый товар"
    assert product.description == "Описание тестового товара"
    assert product.price == 100
    assert product.quantity == 5


def test_product_attributes_types():
    """Тест типов атрибутов Product."""
    product = Product("Тестовый товар", "Описание тестового товара", 100.0, 5)

    assert isinstance(product.name, str)
    assert isinstance(product.description, str)
    assert isinstance(product.price, float)  # Цена должна быть float
    assert isinstance(product.quantity, int)


def test_empty_category():
    """Тест создания пустой категории."""
    Category.total_categories = 0
    Category.total_products = 0

    category = Category("Пустая категория", "Описание", [])

    assert category.name == "Пустая категория"
    assert category.description == "Описание"
    assert category.products == []
    assert Category.total_categories == 1
    assert Category.total_products == 0


def test_category_with_products():
    """Тест создания категории с продуктами."""
    Category.total_categories = 0
    Category.total_products = 0

    product1 = Product("Товар 1", "Описание 1", 100.0, 1)
    product2 = Product("Товар 2", "Описание 2", 200.0, 2)

    category = Category("Категория", "Описание", [product1, product2])

    assert len(category.products) == 2
    assert Category.total_categories == 1
    assert Category.total_products == 2
