class car:
    def __init__(self,color,price,kilometer):
        self.color=color;
        self.price=price;
        self.kilometer=kilometer;
    def __gt__(self,other):
        if(self.price > other.price):
            return True
        else:
            return False
        
        

    def __add__(self,other):
        return self.kilometer+other.kilometer
        
car1=car("red",2000000,2000)
car2=car("blue",40000000,3000)

if(car1>car2):
    print("car1 price is high")
else:
    print("car2 price is high")
print("total kilometer of 2 car:",car1+car2)
