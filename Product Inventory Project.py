class Product:
    def __init__(self, uid, price, quantity, name, category):
        self.uid = uid
        self.price = price
        self.quantity = quantity
        self.name = name
        self.category = category

    def __str__(self):
        return f"ID: {self.uid}, Name: {self.name}, Price: {self.price}," \
               f" Category: {self.category}, Quantity: {self.quantity}"


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.uid] = product

    def sum_inventory_value(self):
        sum_inv = sum(item.price for item in self.products.values())
        return f"Price of entire inventory: {sum_inv}"

    def print_products_in_category(self, category):
        filtered_products = self.filter_inventory(category)
        return [str(item) for item in filtered_products]

    def sum_category(self, category):
        cat_sum = sum(item.price for item in self.filter_inventory(category))
        return f"Price of category {category}: {cat_sum}"

    def filter_inventory(self, category):
        return [item for item in self.products.values() if item.category == category]

    def print_inventory(self):
        return [str(product) for product in self.products.values()]

