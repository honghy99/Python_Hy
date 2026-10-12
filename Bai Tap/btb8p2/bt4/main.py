from payment_gateway import PaymentGateway
from momo_payment import MomoPayment
from credit_card_payment import CreditCardPayment

# ===== Bài 4: Tính Trừu tượng =====
payments = [MomoPayment(), CreditCardPayment()]
for payment in payments:
    payment.process_payment(500000)

# Lớp trừu tượng không thể tạo đối tượng trực tiếp -> sẽ bị lỗi TypeError
try:
    gateway = PaymentGateway()
except TypeError as e:
    print(f"Lỗi: {e}")
