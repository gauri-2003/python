class ParkingSystem:
    def __init__(self,big,medium,small):
        self.sp=[0,big,medium,small]

    def addCar(self, carType):
        if(self.sp[carType] >0):
            self.sp[carType]-=1
            return True
        return False
    

ps = ParkingSystem(3 ,2, 1)
print(ps.addCar(2))
print(ps.addCar(2))
print(ps.addCar(1))