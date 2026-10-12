from payment_gateway import PaymentGateway


class CreditCardPayment(PaymentGateway):
    def process_payment(self, amount):
        print(f"Đang xử lý thanh toán thẻ tín dụng số tiền {amount:,}... Vui lòng nhập thông tin thẻ.")


if __name__ == "__main__":
    CreditCardPayment().process_payment(1000)
