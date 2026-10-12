# class Product:
#     def __init__(self, name, price, quality):
#         self.name = name
#         self.price = price
#         self.quality = quality
#     def get_total_price(self, quantity):
#         return self.price * quantity
# product = Product("Laptop", 1000, "High")
# print(f"Product: {product.name}, Price: {product.price}, Quality: {product.quality}, Total Price for 5 units: {product.get_total_price(5)}")


# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def get_total_price(self):
#         return self.price * self.quantity

#     def display_info(self):
#         print(f"Sản phẩm: {self.name}, Đơn giá: {self.price}, "
#               f"Số lượng: {self.quantity}, Tổng giá trị: {self.get_total_price()}")


# product = Product("Laptop", 1000, 5)
# product.display_info()
# # Sản phẩm: Laptop, Đơn giá: 1000, Số lượng: 5, Tổng giá trị: 5000


# class Calculator:
#     def add(self, a, b):
#         return a + b

#     def subtract(self, a, b):
#         return a - b

#     def multiply(self, a, b):
#         return a * b

#     def divide(self, a, b):
#         try:
#             return a / b
#         except ZeroDivisionError:
#             print("Lỗi: Không thể chia cho 0")
#             return None


# calc = Calculator()
# print(calc.add(10, 6))       # 15
# print(calc.subtract(10, 5))  # 5
# print(calc.multiply(10, 5))  # 50
# print(calc.divide(10, 5))    # 2.0
# print(calc.divide(10, 0))    # Lỗi: Không thể chia cho 0 → None


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = ("id", "username")
        self.password_locator = ("id", "password")
        self.login_button_locator = ("id", "login-btn")

    def enter_username(self, username):
        print(f"Tìm element {self.username_locator} và nhập: {username}")

    def enter_password(self, password):
        print(f"Tìm element {self.password_locator} và nhập: {password}")

    def click_login(self):
        print(f"Tìm element {self.login_button_locator} và click")

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()


driver = "FakeDriver"   # giả lập, không cần Selenium thật
login_page = LoginPage(driver)
login_page.login("admin", "123456")

