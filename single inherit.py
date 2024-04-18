class Box:
    def __init__(self,Name,Rlno):
        self.name=Name 
        self.rlno=Rlno
class Sbox:
    def __init__(self,Fees):
        self.fees=Fees
    
class Cbox(Box,Sbox):
    def __init__(self,Name,Rlno,Fees,Sem):
        self.sem=Sem
        Box.__init__(self,Name,Rlno)
        Sbox.__init__(self,Fees)
obj1=Cbox("mickey mouse",2,2000,4)
print(obj1.name)
print(obj1.rlno)
print(obj1.fees)
print(obj1.sem)


