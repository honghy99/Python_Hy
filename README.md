# Python_Hy

Kho lưu trữ bài học và bài tập Python của mình, đi từ kiến thức cơ bản (biến, kiểu dữ liệu, chuỗi, vòng lặp) đến xử lý file và lập trình hướng đối tượng (OOP).

## Cấu trúc thư mục

```
Python_Hy/
├── Anhtester/          # Code thực hành theo từng buổi học
│   ├── buoi1/          # Làm quen Python
│   ├── buoi2/          # Biến, kiểu dữ liệu: number, boolean, list, tuple, set, dictionary, toán tử
│   ├── buoi3/          # Chuỗi: slicing, split, join, replace, strip, toán tử in
│   ├── buoi4/          # Điều kiện if/elif/else, vòng lặp for/while, range
│   ├── buoi5/          # Xử lý ngoại lệ (try/except, raise)
│   └── buoi6/          # Đọc/ghi file JSON và Excel (openpyxl)
│       └── data/       # File dữ liệu mẫu (.json, .xlsx)
│
└── Bai Tap/            # Bài tập về nhà
    ├── baitap.py       # Biến, phép tính, tính BMI
    ├── bt-b3.py        # Xử lý chuỗi
    ├── btb4.py         # Điều kiện và vòng lặp
    ├── btb5.py         # Xử lý ngoại lệ
    ├── btb6.py         # Đọc Excel students.xlsx -> ghi ra report.json
    ├── btb8p1.py       # Class và đối tượng
    ├── btb8p2/         # 4 tính chất của OOP (mỗi bài một thư mục)
    │   ├── bt1/        # Đóng gói (Encapsulation) - Phone
    │   ├── bt2/        # Kế thừa (Inheritance) - Document, Article, Email
    │   ├── bt3/        # Đa hình (Polymorphism) - Giao hàng
    │   ├── bt4/        # Trừu tượng (Abstraction) - Thanh toán online
    │   └── nang_cao/
    │       ├── bt1/    # Hệ thống Element (BaseElement, Button, Checkbox)
    │       └── bt2/    # DriverFactory với @staticmethod
    └── Data/           # Dữ liệu cho bài tập
```

## Yêu cầu

- Python 3.10 trở lên
- Thư viện `openpyxl` (dùng cho các bài đọc/ghi Excel)

```
pip install openpyxl
```

## Cách chạy

Chạy một file bài tập bất kỳ:

```
python "Bai Tap/btb4.py"
```

Các bài OOP trong `btb8p2` được tách thành nhiều file, mỗi bài có một file `main.py` để chạy:

```
python "Bai Tap/btb8p2/bt1/main.py"
python "Bai Tap/btb8p2/nang_cao/bt2/main.py"
```

### Lưu ý

- Các file trong `Anhtester/buoi6` dùng đường dẫn tương đối, nên cần `cd` vào thư mục đó rồi mới chạy:
  ```
  cd Anhtester/buoi6
  python test_json.py
  ```
- Một số bài dùng `input()` để nhập dữ liệu từ bàn phím (ví dụ `baitap.py`, `buoi5/bbth2.py`), cần chạy trong terminal để nhập.

## Tóm tắt bài tập OOP (`btb8p2`)

| Bài | Tính chất | Nội dung chính |
|-----|-----------|----------------|
| bt1 | Đóng gói | Thuộc tính private `__battery_level`, chỉ thay đổi qua `use_app()` / `charge_phone()` |
| bt2 | Kế thừa | `Article`, `Email` kế thừa `Document`, gọi `super().__init__()` và override `show_info()` |
| bt3 | Đa hình | Hàm `get_shipping_cost()` dùng được với mọi đối tượng có `calculate_fee()` |
| bt4 | Trừu tượng | Lớp trừu tượng `PaymentGateway` (module `abc`) bắt lớp con phải có `process_payment()` |
| nâng cao bt1 | Kết hợp cả 4 | `BaseElement` trừu tượng với locator private, lớp con `Button`, `Checkbox` |
| nâng cao bt2 | Factory | `DriverFactory.get_driver()` là `@staticmethod`, raise `ValueError` khi trình duyệt không hỗ trợ |

## Tác giả

Hồng Hy ([@honghy99](https://github.com/honghy99))
