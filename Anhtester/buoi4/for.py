# # for - vòng lặp
# fruits = ["mango", "durian", "apple", "cherry"]
# for fruit in fruits:
#     print("I like:", fruit)

# for s in "Automation":
#     print(s)

# employee = {"name": "lan", "age": 18, "Email": "123@gmail"}
# for key in employee:
#     print(employee[key])

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for number in numbers:
#     print(number)
#     if number==2:
#         print("done")
#         break

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    if (number % 2 == 0 and number >5):
        continue
    print(number)
        
