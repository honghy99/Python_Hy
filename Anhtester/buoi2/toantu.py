# x, y = 10, 3
# print("tổng =", x + y)  # Cộng: 13
# print(f"tổng = {x + y}", f"hiệu = {x - y}")
# print(x - y)  # Trừ: 7
# print(x * y)  # Nhân: 30
# print(x / y)  # Chia thực: 3.333...
# print(x // y) # Chia lấy nguyên: 3
# print(x % y)  # Chia lấy dư: 1
# print(x ** y) # Lũy thừa (10^3): 1000

# Toán tử So sánh (Comparison)
print(10 > 5)   # Lớn hơn -> True
print(10 == 5)  # Bằng nhau -> False (Lưu ý: '==' khác với gán '=')
print(10 != 5)  # Khác nhau -> True
#Toán tử Logic (Logical)
a, b = True, False
print("kq1", a and b)  # Sai (Cả 2 phải True mới trả về True)
print("kq", a or b)   # Đúng (Chỉ cần 1 cái True là True)
print("kq3", not a)    # Sai (Phủ định của True là False)​
print(f"kq1 = {a and b}", f"kq1 = {a or b}")
#Toán tử Gán rút gọn (Assignment)
x = 5
x = x + 3
print(x)
x += 3   # Tương đương x = x + 3. Kết quả: x = 8
print(x)
#Toán tử Thành viên (Membership)
fruits = ["apple", "banana"]
print("apple" in fruits)      # True
print("orange" not in fruits) # True

#Toán tử Nhận dạng (Identity)
a = [1, 2]
b = [1, 2]
print(a == b)  # True (Giá trị giống nhau)
print(a is b)  # False (Nằm ở 2 vùng nhớ khác nhau)