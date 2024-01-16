class ParkingSystem:
    def __init__(self, big,medium,small):
        self.cnt = [0, big, medium, small]

    def addCar(self, carType):
        if self.cnt[carType] == 0:
            print("False")
        self.cnt[carType] -= 1
        print("True")



# Your ParkingSystem object will be instantiated and called as such:
parksys = ParkingSystem(1,1,0)
parksys.addCar(1)
parksys.addCar(2)
parksys.addCar(3)
parksys.addCar(1)