class Fighter:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.damage = 10
    
    
    def attack(self, other_fighter):
        other_fighter.health -= self.damage
        print("{} attacks {}".format(self.name, other_fighter.name))
        print("{} losses {}".format(self.name, other_fighter.name))
        return ("{} : {}".format(other_fighter.name, other_fighter.health))
    
    
    def __str__(self):
        return("{} : {}".format(self.name, self.health))

    
A = Fighter('Ken')
B = Fighter('Ryu')
