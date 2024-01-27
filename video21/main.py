class Robot:
    population = 0
    """this is a robot class"""
    def __init__(self,name,year):
        self.name = name
        self.year = year
        Robot.population += 1
    def __del__(self):
        print("robot is distroyed")
    def SetEnergy(self,energy):
        self.energy = energy
    def Relative(self,Rel):
        self.Rel = Rel
        print(Rel)    
        


r1 = Robot("rr1",2001)
r1.SetEnergy(400)
r2  =Robot("rr2",2024)

print(r1.__doc__)
print(r1.__dict__)
r1.Relative(["linus","collins","elvis","paul"])
#r2.Relative(["us","ins","is","ul"])
print(r1.energy)
print(getattr(r1,"energy"))
print(getattr(r1,"notavailable","N/A"))
print(Robot.population)
print(r1.Rel)
