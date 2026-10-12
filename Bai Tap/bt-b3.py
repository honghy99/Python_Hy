text = "  hello world  "
#Dùng len() để đếm số ký tự (bao gồm cả khoảng trắng).
print(len(text))
#Dùng strip() để bỏ khoảng trắng đầu và cuối, sau đó in lại chiều dài.
print(text.strip())
# text1=(text.strip())
print(len(text.strip()))
#==============================================
name = "Hong Hy"
#In ra chữ hoa toàn bộ.
print(name.upper())
# In ra chữ thường toàn bộ.
print("viet thuong la:", name.lower())
# In ra dạng capitalize (chữ cái đầu viết hoa).
print("In ra dạng capitalize (chữ cái đầu viết hoa):", name.capitalize())
# In ra dạng title (mỗi từ viết hoa chữ cái đầu).
print("In ra dạng title (mỗi từ viết hoa chữ cái đầu):", name.title())
#===================================================
s = "Automation Testing"
# Lấy ra từ "Automation".
print(s[0:10:])
# Lấy ra từ "Testing".
s1=s[11::]
print(s1)
# Lấy 5 ký tự đầu tiên.
print(s[:5:])
# Lấy 3 ký tự cuối cùng.
print(s[-3::])
#==================================================
messy_phone = " 090-123 4567 "
# Dùng strip() để bỏ khoảng trắng.
print(messy_phone.strip())
#Dùng replace() để bỏ dấu - và khoảng trắng.
print(messy_phone.replace("-","").replace(" ",""))
print(messy_phone.replace(" ",""))
#In ra số điện thoại chuẩn hóa: 0901234567.
phone_clean = messy_phone.replace("-","").replace(" ","")
print("STD chuan la:",phone_clean)
print(f"SDT chuan la:{phone_clean}")

#=========================================
fruits = ["apple", "banana", "cherry"]
#Dùng join() để nối list thành một chuỗi dạng: "apple, banana, cherry".
F = ", ".join(fruits)
print(F)

#========================================
log = "ERROR: Login failed at 10:45"

error = "ERROR"
if error in log: 
    print("❌ Có lỗi xảy ra")
else:
    print("✅ Hệ thống bình thường")