class PaymentProcessor:
    @staticmethod
    def process_payment(total_sum):
        print(f"Total: {total_sum}")
        payment = float(input("Payment: "))
        if payment < total_sum:
            print("Insufficient payment. Transaction failed.")
            return None
        change = payment - total_sum
        print(f"Change: {change}")
        return payment

