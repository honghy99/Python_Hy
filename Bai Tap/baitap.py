# info = ["Hy" , 18 ]
# print("Tên:" , info[0], "Tuổi:" , info[-1])
# a = 6
# b = 7
# c = { "a+b =": a +b, 
#      "a-b=": a -b,
#      "a*b=": a * b,
#     "a/b=": a/b,
#     "a/b lấy dư =": a%b,
#      "a^b=": a ** b }
# print(c)

# print("a+b =", a +b, 
#       "a-b=", a -b, 
#       "a*b=", a * b, 
#       "a/b=", a/b, 
#       "a/b lấy dư =", a%b, 
#       "a^b=", a ** b)

# s = int(input("Nhập số giây: "))

# gio = s // 3600          # 1 giờ = 3600 giây
# phut = (s % 3600) // 60  # phần dư sau khi lấy giờ, chia cho 60
# giay = s % 60            # phần dư cuối cùng

# print(f"{gio}:{phut}:{giay}")

s = float(input("Nhập chiều cao (cm) "))
y = int(input("nhập cân nặng (kg) "))
z = s * 0.01
bmi= y/(z*z)

print("chỉ số bmi =", bmi)
