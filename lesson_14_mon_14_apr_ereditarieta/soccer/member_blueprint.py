class MembroSquadra:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def describe(self):
        return f"{self.__class__.__name__} name is: {self.name}, he is {self.age} years old"

