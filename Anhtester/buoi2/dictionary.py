employee = {
            "Name":"Ngoc", 
            "Age":"18", 
            "PhoneNum":"0333560678"
            }
employee["address"] = "Ha Noi"
# print(employee["Age"])
# print(employee["PhoneNum"])
employee.update({"Age":25})
employee["Name"] ="Hy"
del employee["PhoneNum"]
employee.pop("Age")
print(employee)