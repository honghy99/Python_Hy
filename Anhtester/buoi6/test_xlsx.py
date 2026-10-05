import openpyxl

try: 
    wb = openpyxl.load_workbook("../buoi6/data/login_data.xlsx")
    sheet = wb.active
    cell1 = sheet["B2"].value
    print("Value user:", cell1)
except FileNotFoundError:
    print("file not found")
except Exception as e:
    print(f"{e}")
