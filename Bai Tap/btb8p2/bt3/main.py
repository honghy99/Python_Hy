from delivery import MotorbikeDelivery, GrabDelivery, TruckDelivery


# Hàm nằm ngoài các class: không cần biết delivery_method là loại nào,
# chỉ cần đối tượng đó có phương thức calculate_fee
def get_shipping_cost(delivery_method, distance):
    fee = delivery_method.calculate_fee(distance)
    print(f"{type(delivery_method).__name__} - {distance} km: {fee:,} VND")


# ===== Bài 3: Tính Đa hình =====
distance = 10
methods = [MotorbikeDelivery(), GrabDelivery(), TruckDelivery()]

for method in methods:
    get_shipping_cost(method, distance)
