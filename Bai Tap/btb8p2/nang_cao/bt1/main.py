from base_element import BaseElement
from button import Button
from checkbox import Checkbox

# ===== Bài nâng cao 1: Hệ thống Element =====
login_button = Button(("id", "login-btn"))
remember_checkbox = Checkbox(("id", "remember-me"))

# Đa hình: cùng gọi click() nhưng mỗi element xử lý khác nhau
for element in [login_button, remember_checkbox]:
    element.click()

remember_checkbox.is_selected()
print("Locator của button:", login_button.get_locator())

# Đóng gói: không truy cập trực tiếp được __locator
try:
    print(login_button.__locator)
except AttributeError:
    print("Không thể truy cập trực tiếp __locator từ bên ngoài class")

# Trừu tượng: không tạo được đối tượng từ BaseElement
try:
    BaseElement(("id", "abc"))
except TypeError as e:
    print(f"Lỗi: {e}")
