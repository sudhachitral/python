class Bike:
    def __init__(self, speed, brand, wheelsCount):
        self.speed = speed 
        self.brand = brand
        self.wheelsCount = 12
 
    def helperFunction(self):
        print("One")
        print("Two")
 
    def printWheels(self):
        print("Wheels count is:", self.wheelsCount)
        self.helperFunction()
 
    def printBrandName(self):
        self.printWheels()
        print("Brand name is:", self.brand)
 
    def printSpeed(self):
        self.printWheels()
        print("Sorry, I am not going to print speed")
        self.printBrandName()
 
bike1 = Bike(90, "R-1 5", 2)
bike2 = Bike(115, "GT", 2)
bike3 = Bike(65, "Pulsar", 4)
print(bike2.brand)
bike2.printBrandName()
bike3.printSpeed()
bike1.printWheels()
