# def safe_divide():
#     try:
#         a = float(input("Số bị chia: "))
#         b = float(input("Số chia: "))
#         ketqua = a / b
#     # except ValueError:
#     #     print("Lỗi: Bạn phải nhập số!")
#     except ZeroDivisionError:
#         print("Không thể chia cho 0")
#     else:
#         print("Kết quả:", a / b)


# safe_divide()

def set_age(age):
    if not isinstance(age, int):
        raise TypeError("Tuổi phải là một số nguyên.")
    if age < 0:
        raise ValueError("Tuổi không thể là một số âm.")
    print(f"Tuổi đã được đặt là: {age}")

try:
    set_age(-5)
except (TypeError, ValueError) as e:
    print(f"Lỗi khi đặt tuổi: {e}")
