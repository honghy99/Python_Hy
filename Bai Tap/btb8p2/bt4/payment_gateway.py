# Bài 4: Tính Trừu tượng (Abstraction) - Lớp trừu tượng PaymentGateway
from abc import ABC, abstractmethod


class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        # Chỉ khai báo, không viết nội dung. Lớp con bắt buộc phải triển khai
        pass
