# trên 2 điều kiện 
# if dieu_kien_1:
#     # Thực thi nếu dieu_kien_1 là True
# elif dieu_kien_2:
#     # Thực thi nếu dieu_kien_1 là False VÀ dieu_kien_2 là True
# else:
#     # Thực thi nếu tất cả các điều kiện trên đều False

# score =5.8
# if score>= 9:
#     print("very good")
# elif score>=8:
#     print("good")
# elif score>= 6.5:
#     print("normal")
# else:
#     print("weak")

sv = [9, 8, 7, 6, 5]
dtb = sum(sv)/len(sv)
print("dtb là:", dtb)
if dtb>= 9:
    print("very good")
elif dtb>=8:
    print("good")
elif dtb>= 6.5:
    print("normal")
else:
    print("weak")
