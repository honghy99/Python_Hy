import json

with open ("../buoi6/data/recipe_data.json", "r", encoding="utf-8") as f: 
    try: 
        recipe_data = json.load(f)
        print(f"Tên món ăn : {recipe_data["Tên món ăn"]}")
        print(f"Thời gian chuẩn bị : {recipe_data["Thời gian chuẩn bị"]}")
        print(f"Nguyên liệu : {recipe_data["Nguyên liệu"]}")
    except json.JSONDecodeError:
        print("Json error")
    except FileExistsError:
        print("file not found")
        
