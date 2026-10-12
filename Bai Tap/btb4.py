
# expected_messages = ["Login successful", "Welcome"]
# actual_message = "Welcome"
# if actual_message in expected_messages:
#     print ("Message valid")
# else:
#     print("Message invalid")

#2.Tìm số chia hết cho 7 đầu tiên trong dãy từ 1 đến 100 và in ra màn hình

# for i in range(1,101):
#     if i % 7 == 0:
#         print("số chia hết cho 7 đầu tiên trong dãy từ 1 đến 100 là:", i)
#         break 
 
 	
# 3. Phân loại học lực theo điểm trong list sau               
# scores =[95, 82, 67, 45, 88, 90, 50]
# for score in scores:
#     if score >= 90:
#         print(score, "Xuất sắc ")
#     elif score >= 70:
#         print(score,"Khá")
#     elif score >= 50:
#         print(score,"TB")
#     else:
#         print(score,"Yếu")

 
 	
# 4. In ra bảng cửu chương 2 & 3

# for i in range(1,11):
#     print(i,"*2 =", i*2)
# for e in range(1,11):
#     print(e,"*3 =", e*3)
#5
products = ["iPhone 13", "Samsung Galaxy", "MacBook Pro 16 inch", "Oppo Reno"]
for product in products:
    if product == "MacBook Pro 16 inch":
        print ("Đã tìm thấy sản phẩm")
        break
else:
        print("Không tìm thấy sản phẩm")

#6 
# numbers = [2, 5, 8, 11, 14, 17, 20]
# for number in numbers:
#     if number % 2 == 0:
#         print(number)

# print(sum(numbers))

# numbers = [2, 5, 8, 11, 14, 17, 20]

# for number in numbers:
#     print(f"\nBảng cửu chương {number}:")
    
#     for i in range(1, 11):
#         print(f"{number} x {i} = {number * i}")
