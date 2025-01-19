from assignment3.paymet_Processor import PaymentProcessor
from assignment3.product_Manager import ProductManager

class Assignment3:
    @staticmethod
    def get_product():
        product_manager = ProductManager()
        print("Supermarket")
        print("===========")

        while True:
            try:
                user_input = input("Please select product (1-10) 0 to Quit: ")
                if user_input == "0":
                    break
                product_num = int(user_input)
                price = product_manager.select_product(product_num)
                product_manager.add_to_total(price)
            except ValueError:
                print("Invalid input.")

        total_sum = product_manager.get_total_sum()
        if total_sum > 0:
            PaymentProcessor.process_payment(total_sum)
        else:
            print("No items purchased. Exiting.")


if __name__ == "__main__":
    Assignment3.get_product()
