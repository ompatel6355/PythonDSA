class Vehicle:
    def Start(self):
        print("Vehicle started")

class Car(Vehicle):
    # def __init__(self, Vehicle):
    #     self.name = Vehicle
    def drive(self):
        print("is getting driving")
    
c = Car()
c.drive()
c.Start()