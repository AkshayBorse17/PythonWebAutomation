class ParkingSystem:

    def __init__(self, big, medium, small):
        self.slots = [big, medium, small]

    def addCar(self, carType):
        if 1 <= carType <= 3 and self.slots[carType - 1] > 0:
            self.slots[carType - 1] -= 1
            return True
        return False

parksys = ParkingSystem(1, 1, 0)

print(parksys.addCar(1))
print(parksys.addCar(2))
print(parksys.addCar(3))
print(parksys.addCar(1))
