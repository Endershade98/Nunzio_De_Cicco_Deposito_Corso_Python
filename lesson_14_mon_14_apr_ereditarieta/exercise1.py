

class Animal:
    
    def __init__(self, name, age, animal_sound):
        self.name = name
        self.age = age
        self.sound = animal_sound
    
    def make_a_sound(self):
        return f"{self.name} is {self.age} years old and make a {self.sound}"


class Lion(Animal):
    
    def __init__(self, name, age, animal_sound, prey, habitat):
        Animal.__init__(name, age, animal_sound)
        self.prey = prey
        self.habitat = habitat
        
    def make_a_sound(self):
        super().make_a_sound()
        return f"{self.__name__} eats {self.prey}"
    
    def hunt(self):
        return f"{self.__name__} hunting in the {self.habitat}"
    

class Penguin(Animal):
    
    def __init__(self, name, age, animal_sound, habitat):
        Animal.__init__(name, age, animal_sound)
        self.habitat = habitat
        
    
    def make_a_sound(self):
        super().make_a_sound()
        return f"lives in {self.habitat}"
    
    def lives_in(self):
        return f"{self.__name__} swim in the {self.habitat}"
    

class Giraffe(Animal):
    
    def __init__(self, name, age, animal_sound, food, type):
        Animal.__init__(name, age, animal_sound)
        self.food = food
        self.type = type
    
    def make_a_sound(self):
        super().make_a_sound()
        return f"{self.__name__} eats {self.food}"
    
    def show_type(self):
        return f"{self.__name__} is a {self.type}"

        