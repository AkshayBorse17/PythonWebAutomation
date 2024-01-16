
class ParkingSystem:
    def __init__(self, big, medium, small):
        self.count = [0, big, medium, small]

    def addCar(self, car):
        if self.count[car] == 0:
            return False
        self.count[car] -= 1
        return True


obj = ParkingSystem(3,2,1)
print("b",obj.addCar(1))
print("s",obj.addCar(3))
print("m",obj.addCar(2))
print("b",obj.addCar(1))
print("m",obj.addCar(2))
print("s",obj.addCar(3))
print("s",obj.addCar(3))
print("b",obj.addCar(1))
print("m",obj.addCar(2))
