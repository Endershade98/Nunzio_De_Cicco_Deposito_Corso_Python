
x = 10

def somma(y, z):
    return x + y + z
   
pi = 3.14
class Circle:
 
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return pi * (self.radius**2)
    

# esempio di ereditarietà diretta
class Animal:
    
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print(f"{self. name} is speaking")


class Dog(Animal):
    
    def speak(self): # overriding di speak() di Animal il metodo è autonomo
        print(f"{self.name} says woolf!")
    
    
animal = Animal("Animal").speak() # non collegati a livello logico ma funzionale
print(animal)

dog = Dog("Doggo").speak()

print(dog)