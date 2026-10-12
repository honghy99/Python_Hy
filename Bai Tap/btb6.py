import json
import openpyxl
from pathlib import Path

thu_muc = Path(__file__).parent
file_excel = thu_muc / "Data" / "students.xlsx"
file_json = thu_muc / "report.json"

try:
    wb = openpyxl.load_workbook(file_excel)
    sheet = wb.active

    # Dòng 1 là tiêu đề: ID, Họ tên, Điểm, Xếp loại
    tieu_de = [cell.value for cell in sheet[1]]

    students = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        if all(v is None for v in row):   # bỏ qua dòng trống
            continue
        sv = dict(zip(tieu_de, row))
        sv["Điểm"] = float(sv["Điểm"])   # Excel lưu 9.0 thành 9 -> ép về float
        students.append(sv)

    with open(file_json, "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=4)

    print("Đã ghi xong file report.json")

except FileNotFoundError:
    print("Không tìm thấy file students.xlsx")
except Exception as e:
    print(f"Lỗi: {e}")