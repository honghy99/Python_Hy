import openpyxl, json
wb = openpyxl.load_workbook("../buoi6/data/student.xlsx")
sheet = wb.active
verygood_student = []
good_student = []
for row in sheet.iter_rows(min_row=2, values_only=True):
    stt, id, name, score = row
    score = float(score)
    if (score>=9):
        verygood_student.append({
            "ID": id,
            "Name": name, 
            "score": score
        })
    elif (7 < score <9 ):
        good_student.append({
            "ID": id,
            "Name": name, 
            "score": score
        })
with open("../buoi6/data/verygoods.json", "w", encoding="utf8") as f:
    json.dump(verygood_student, f, ensure_ascii= False, indent=2)
with open("../buoi6/data/goods.json", "w", encoding="utf8") as f:
    json.dump(good_student, f, ensure_ascii= False, indent=2)
print(" Completed write to json file")