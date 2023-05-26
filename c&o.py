class Robot:
    def __init__(self,name,colour,weight):
        self.name=name
        self.colour=colour
        self.weight=weight
    def introduce_self(self):
        print("My name is " + self.name)

r1= Robot()
r1.name="tom"
r1.colour = "red"
r1.weight = "30"

r2= Robot()
r2.name="Mot"
r2.colour = "Blue"
r2.weight = "60"

r1.introduce_self()
r2.introduce_self()

