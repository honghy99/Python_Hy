# Bài 1: Tính Đóng gói (Encapsulation) - Chiếc Điện thoại
class Phone:
    def __init__(self):
        # __battery_level là thuộc tính private, bên ngoài class không truy cập trực tiếp được
        self.__battery_level = 100

    def use_app(self, hours):
        # Mỗi giờ sử dụng giảm 10%, pin không được nhỏ hơn 0
        self.__battery_level -= hours * 10
        if self.__battery_level < 0:
            self.__battery_level = 0

    def charge_phone(self, hours):
        # Mỗi giờ sạc tăng 20%, pin không được vượt quá 100
        self.__battery_level += hours * 20
        if self.__battery_level > 100:
            self.__battery_level = 100

    def display_battery(self):
        print(f"Dung lượng pin hiện tại: {self.__battery_level}%")


phone = Phone()
phone.display_battery()   # 100%

phone.use_app(3)
phone.display_battery()   # 70%

phone.use_app(10)
phone.display_battery()   # 0% (không bị âm)

phone.charge_phone(2)
phone.display_battery()   # 40%

phone.charge_phone(5)
phone.display_battery()   # 100% (không vượt quá 100)

# Thử truy cập trực tiếp thuộc tính private -> sẽ bị lỗi
try:
    print(phone.__battery_level)
except AttributeError:
    print("Không thể truy cập trực tiếp __battery_level từ bên ngoài class")


# Bài 2: Tính Kế thừa (Inheritance) - Các loại Tài liệu
class Document:
    def __init__(self, title):
        self.title = title

    def show_info(self):
        print(f"Tiêu đề: {self.title}")


class Article(Document):
    def __init__(self, title, author):
        super().__init__(title)   # gọi __init__ của lớp cha để lưu title
        self.author = author

    def show_info(self):          # override phương thức của lớp cha
        print(f"Bài báo: {self.title} - Tác giả: {self.author}")


class Email(Document):
    def __init__(self, title, sender):
        super().__init__(title)
        self.sender = sender

    def show_info(self):
        print(f"Email: {self.title} - Người gửi: {self.sender}")


doc = Document("Tài liệu chung")
article = Article("Python cơ bản", "Hồng Hy")
email = Email("Họp dự án", "admin@company.com")

for item in [doc, article, email]:
    item.show_info()
