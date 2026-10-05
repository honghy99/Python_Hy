try:
    a = float(input("Nhập số a: "))
    b = float(input("Nhập số b: "))
    ketqua = a / b
    print("Kết quả:", ketqua)
except (ValueError, ZeroDivisionError) as e:
    if isinstance(e, ValueError):
        print("Lỗi: Bạn phải nhập số, không được nhập chữ hoặc ký tự khác!")
    else:
        print("Lỗi: Số chia phải khác 0!")