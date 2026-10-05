# numbers = {1, 2, 3, 4, 5, 6, 3 ,2 ,1}
# print(numbers)

# emails = {"a@gmail.com", "b@gmail.com", "c@gmail.com", "d@gmail.com", "b@gmail.com" }
# print(emails)
# #add
# emails.add("e@gmail.com")
# print(emails)
# #delete
# emails.remove("e@gmail.com")
# emails.discard("e@gmail.com")
# print(emails)
# emails = ["a@gmail.com", "b@gmail.com", "c@gmail.com", "d@gmail.com", "b@gmail.com" ]
# print(set(emails))

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)   # Hợp: {1, 2, 3, 4, 5, 6}
print(A & B)   # Giao: {3, 4}
print(A - B)   # Hiệu: {1, 2}
print(A ^ B)   # Phần tử chỉ có ở 1 tập hợp: {1, 2, 5, 6}
