# 请你给一个停车场设计一个停车系统。
# 停车场总共有三种不同大小的车位：大，中和小，每种尺寸分别有固定数目的车位。
# 请你实现ParkingSystem类：
# ParkingSystem(int big, int medium, int small)初始化ParkingSystem类，三个参数分别对应每种停车位的数目。
# bool addCar(int carType)检查是否有carType对应的停车位。carType有三种类型：大，中，小，分别用数字1，2和3表示。
# 一辆车只能停在carType对应尺寸的停车位中。如果没有空车位，请返回false，否则将该车停入车位并返回true。
# ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
# [[1, 1, 0], [1], [2], [3], [1]]
# 输出：
# [null, true, true, false, false]

class ParkingSystem1:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            self.big -= 1
            return self.big >= 0
        elif carType == 2:
            self.medium -= 1
            return self.medium >= 0
        elif carType == 3:
            self.small -= 1
            return self.small >= 0


class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.data = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        self.data[carType - 1] -= 1
        return self.data[carType - 1] >= 0


a = ParkingSystem(1, 1, 1)
print(a.addCar(1))
print(a.addCar(1))
