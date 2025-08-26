from src.models import Product, Category


if __name__ == "__main__":
    # Создаем продукты
    product1 = Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5
    )
    product2 = Product(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8
    )
    product3 = Product(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14
    )

    # Создаем категорию
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения "
        "дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    # Тестируем геттер products
    print("Список товаров в категории:")
    for product_info in category1.products:
        print(f"  - {product_info}")

    print(f"\nОбщее количество товаров в магазине: {Category.total_products}")
    print(f"Количество категорий: {Category.total_categories}")
    print(f"Товаров в этой категории: {category1.product_count}")

    # Добавляем новый товар
    print("\n" + "=" * 50)
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    print(f"Добавляем товар: {product4.name}")

    category1.add_product(product4)
    print(f"После добавления: {category1.product_count} товаров в категории")
    print(f"Общее количество товаров: {Category.total_products}")

    # Тестируем класс-метод new_product
    print("\n" + "=" * 50)
    print("Тестирование класса-метода new_product:")

    new_product_data = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 190000.0,  # Более высокая цена
        "quantity": 3
    }

    new_product = Product.new_product(
        new_product_data,
        category1.products_objects
    )
    print(f"Созданный продукт: {new_product.name}")
    print(f"Цена: {new_product.price} руб.")  # Должна быть 190000.0
    print(f"Количество: {new_product.quantity} шт.")  # Должно быть 8 (5 + 3)

    # Тестируем сеттер цены
    print("\n" + "=" * 50)
    print("Тестирование сеттера цены:")

    print(f"Текущая цена: {new_product.price}")

    # Пытаемся установить отрицательную цену
    new_product.price = -100  # Должно вывести сообщение об ошибке
    print(f"Цена после попытки установить -100: {new_product.price}")

    # Пытаемся установить нулевую цену
    new_product.price = 0  # Должно вывести сообщение об ошибке
    print(f"Цена после попытки установить 0: {new_product.price}")

    # Устанавливаем корректную цену
    new_product.price = 150000
    print(f"Цена после установки 150000: {new_product.price}")

    # Тестируем обработку ошибок
    print("\n" + "=" * 50)
    print("Тестирование обработки ошибок:")

    try:
        category1.add_product("не продукт")  # Должна быть ошибка
    except TypeError as e:
        print(f"✓ Правильно поймана ошибка: {e}")

    try:
        category1.add_product(123)  # Должна быть ошибка
    except TypeError as e:
        print(f"✓ Правильно поймана ошибка: {e}")

    # Финальный вывод
    print("\n" + "=" * 50)
    print("Финальный список товаров:")
    for i, product_info in enumerate(category1.products, 1):
        print(f"{i}. {product_info}")

    # Дополнительные тесты из оригинального кода
    print("\n" + "=" * 50)
    print("Дополнительные тесты:")

    product1 = Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5
    )
    product2 = Product(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8
    )
    product3 = Product(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14
    )

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения "
        "дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(str(category1))
    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)