# #1. Tạo list gồm 5 số, tính tổng tất cả các số trong list.
# city = ["HCM", "Ha Noi", "Da Nang", "Can Tho"]
# print(len(city))
# #2. Viết chương trình in ra tất cả các phần tử của dict {"name": "Lan", "age": 25, "city": "Hà Nội"}.
# info = {
#         "name": "Lan", 
#         "age": 25, 
#         "city": "Hà Nội"
#         }
# print(info)
# #3
# a = 10                                                                                                                                                                                                        
# b = 3.5                                                                                                                                                                                                        
# c = True                                                                                                                                                                                                        
# d = None                                                                                                                                                                                                        
# e = "Python"  
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))

# scores = [9, 7, 10, 8, 6]
# #In ra điểm cao nhất. 
# print("Điểm cao nhất:", max(scores))
# #Tính điểm trung bình.   
# print("Điểm trung bình:", sum(scores) / len(scores))
# #Thêm điểm 5 vào cuối list.
# scores.append(5)
# print("đây là danh sách điểm sau khi thêm", scores)

# #Tạo tuple birthday = (11, 9, 2025) → in ra ngày, tháng, năm.   
# birthday = (11, 9, 2025)
# print("Ngày", birthday[0])
# print("Tháng", birthday[-2])
# print("Năm", birthday[-1])
# #birthday[0] = 12


# #"4. Tạo dictionary student = {""name"": ""Lan"", ""age"": 18, ""email"": ""lan@gmail.com""}.
# student = {"name": "Lan",
#             "age": 18, 
#             "email": "lan@gmail.com"
#             }
# print(student["email"])
# print(student["age"])

# #5. Tạo set emails = {"a@gmail.com", "b@gmail.com", "a@gmail.com"}.

# emails = {"a@gmail.com", "b@gmail.com", "a@gmail.com"}

# print(emails)
# emails.add("c@gmail.com")
# print(emails)
# emails.remove("d@gmail.com") #khi xóa bằng remove trong kiểu dữ liệu set nếu giá trí đó không tồn tại thì sẽ báo lỗi
# emails.discard("d@gmail.com") #khi xóa bằng discard trong kiểu dữ liệu set nếu giá trí đó không tồn tại thì sẽ bỏ qua và không báo lỗi chương trình vẫn tiếp tục những câu lênh sau 


def greet(name):
    return("Hello", name)

x = greet("Lan")
print(x)   # None
