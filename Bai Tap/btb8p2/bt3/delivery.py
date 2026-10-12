# Bài 3: Tính Đa hình (Polymorphism) - Giao hàng
# 3 class riêng biệt, không kế thừa nhau, nhưng đều có cùng phương thức calculate_fee
class MotorbikeDelivery:
    def calculate_fee(self, distance_km):
        return distance_km * 5000


class GrabDelivery:
    def calculate_fee(self, distance_km):
        return distance_km * 7000


class TruckDelivery:
    def calculate_fee(self, distance_km):
        return distance_km * 20000


if __name__ == "__main__":
    print(MotorbikeDelivery().calculate_fee(1))
