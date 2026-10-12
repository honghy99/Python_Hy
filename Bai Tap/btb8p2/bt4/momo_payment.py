from payment_gateway import PaymentGateway


class MomoPayment(PaymentGateway):
    def process_payment(self, amount):
        print(f"Đang xử lý thanh toán Momo số tiền {amount:,}... Vui lòng quét mã QR.")


if __name__ == "__main__":
    MomoPayment().process_payment(1000)
