class vehicle:

    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(vehicle):
    pass


S_bus = Bus("School Volvo",180,12)
print("Vehicle: ",S_bus.name,"Speed: ",S_bus.max_speed,"Mileage: ",S_bus.mileage)