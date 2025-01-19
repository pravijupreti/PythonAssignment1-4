class ProductManager:
    def __init__(self):
        self.prices = [10, 14, 22, 33, 44, 13, 22, 55, 66, 77]
        self.total_sum = 0

    def display_product(self, product_num):
        price = self.prices[product_num - 1]
        print(f"Product: {product_num} Price: {price}")
        return price

    def select_product(self, product_num):
        if 1 <= product_num <= 10:
            return self.display_product(product_num)
        else:
            print("Invalid product number.")
            return 0

    def add_to_total(self, price):
        self.total_sum += price

    def get_total_sum(self):
        return self.total_sum