# Bài 2: Lớp con Email kế thừa Document
# Không đặt tên file là email.py vì sẽ trùng với thư viện email có sẵn của Python
from document import Document


class Email(Document):
    def __init__(self, title, sender):
        super().__init__(title)
        self.sender = sender

    def show_info(self):
        print(f"Email: {self.title} - Người gửi: {self.sender}")


if __name__ == "__main__":
    Email("Test", "admin@company.com").show_info()
