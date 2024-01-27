class Robot:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def __del__(self):
        print(f"{self.name} is deleted") 
    def __str__(self):
        my_str = f"I am {self.name} and an am worth {self.price}"
        return my_str
    def __add__(self,other):
        price = self.price + other.price
        return price
        
        
r1 = Robot("chatgpt",20)
r2 = Robot("Grok",30)

print(r1)
print(r2)   
pt = r1+r2
print(pt)