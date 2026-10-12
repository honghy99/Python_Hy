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


if __name__ == "__main__":
    Phone().display_battery()
