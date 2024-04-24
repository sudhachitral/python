class Card:
    def _init_(self,Product,Imageurl,Devicetype,Price,Rating):
        self.product=Product
        self.image=Imageurl
        self.device=Devicetype
        self.price=Price
        self.rating=Rating
        
    def details(self):
        print(self.product)
        print("imageUrl:",self.image)
        print("deviceType:",self.device)
        print("price:",self.price)
        print("rating:",self.rating)
        print()
        
Product1=Card("Product - 1 :","Dummy-url 1","Mobile",56000,4.5)
Product1.details()

Product2=Card("Product - 2 :","Dummy-url 2","Laptop",94000,4.8)
Product2.details()

Product3=Card("Product - 3 :","Dummy-url 3","Smart-watch",18000,3.5)
Product3.details()
