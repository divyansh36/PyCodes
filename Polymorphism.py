class Animals:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs
     
    def des(self):
        print('{} has {} legs'.format(self.name, self.legs))
    
    
    def talk(self):
        pass
    
A= Animals('Peto', 2)


class Dog(Animals):
    def talk(self):
        print('WooF')
    
class Cat(Animals):
    def talk(self):
        print('Meow')
        
        
B = Dog('Pub', 4)
C = Cat('Kitty', 4)


print(A.name)
print(B.legs)
print(B.talk())
