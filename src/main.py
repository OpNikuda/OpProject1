from models import Category, Product


def main():
    product_1 = Product(
        "iPhone 16",
        "Смартфон от Apple",
        999.99,
        1044
    )
    product_2 = Product(
        "Samsung Galaxy",
        "Android смартфон",
        799.99,
        3555
    )

    electronics = Category(
        "Электроника",
        "Гаджеты и устройства",
        [product_1, product_2]
    )

    print(f"Всего категорий: {Category.total_categories}")
    print(f"Всего продуктов: {Category.total_products}")
    print(f"Продукты в категории '{electronics.name}': {len(electronics.products)}")


if __name__ == "__main__":
    main()