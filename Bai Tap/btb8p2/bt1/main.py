from phone import Phone

# ===== Bài 1: Tính Đóng gói =====
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
