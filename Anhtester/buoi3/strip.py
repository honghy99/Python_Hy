name ="  Hong Hy. "
# loại bỏ khoảng trắng 2 đầu chuỗi
print(name.strip())
# loại bỏ khoảng trắng phía trước
print(name.lstrip())
# loại bỏ khoảng trắng phái sau 
print(len(name.rstrip()))

expected = "Login Successful"
actual = "   Login Successful   "

if expected == actual.strip():
    print("✅ Test Passed")
