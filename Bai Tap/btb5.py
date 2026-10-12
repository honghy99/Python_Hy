#1
# try:
#     so = float(input("Nhập một số: "))
#     print("Bình phương:", so ** 2)
# except ValueError:
#     print("Sai định dạng")

#2
# try:
#     with open("../lambaitap/data.txt", "r", encoding="utf-8") as f:
#         print(f.read())
# except FileNotFoundError:
#     print("File không tồn tại")
# finally:
#     print("Kết thúc chương trình")

#3
# from datetime import datetime

# nam_hien_tai = datetime.now().year

# try:
#     nam_sinh = int(input("Nhập năm sinh: "))
#     if nam_sinh > nam_hien_tai:
#         raise ValueError("Năm sinh không thể lớn hơn năm hiện tại.")
# except ValueError as e:
#     print(f"Lỗi: {e}")
# else:
#     print(f"Tuổi của bạn là: {nam_hien_tai - nam_sinh}")