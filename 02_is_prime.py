class Man:
    weight = 70
    iq = 130
    def __init__(self,weight,iq):
        self.weight = weight
        self.iq = iq

    def eat(self):
        self.weight = self.weight+10
        self.iq = self.iq-10

    def fight(self):
        self.weight = self.weight-10
        self.iq = self.iq-10
    def sta(self):
        print(self.weight, self.iq)

class Woman:
    weight = 50
    iq = 120
    def __init__(self,weight,iq):
        self.weight = weight
        self.iq = iq

    def eat(self):
        self.weight = self.weight+10
        self.iq = self.iq-10

    def fight(self):
        self.weight = self.weight-10
        self.iq = self.iq-10

    def sta(self):
        print(self.weight, self.iq)

mys = Man(80,120)
mys.eat()
mys.sta()
mys.fight()
mys.sta()
