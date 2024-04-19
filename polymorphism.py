class Box1:
    def __init__(self,name):
        self.name=name
    def printdetails(self):
        print("printing name",self.name)
class Box2(Box1):
    def __init__(self,roll,name):
        self.roll=roll
        Box1.__init__(self,name)
    def printdetails(self):
        print("printing rollno",self.roll)
obj=Box2(99,"raj")
obj.printdetails()
