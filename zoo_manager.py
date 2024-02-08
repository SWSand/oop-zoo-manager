# ------------------ ANIMAL CLASS ------------------ 

class Animal:
    
    def __init__(self,name,species):
        self.species = species
        self.name = name
        self.sound = "Animal sound"

    def speak(self):
        return f"{self.sound}"
    
    def __Str__(self):
        return f"Species:{self.species} | Name: {self.name}"
    

# ------------------ MAMMAL CLASS ------------------
    
class Mammal(Animal):

    def __init__(self,species,name):
        super().__init__(name,species)
      
    def give_birth(self):
        return (f"{self.species} the {self.name} has given birth")

# ------------------ BIRD CLASS ------------------

class Bird(Animal):

    def __init__(self,species,name,wingspan):
        super().__init__(species,name)

        self.wingspan = wingspan


# ------------------ REPTILE CLASS ------------------ 

class Reptile(Animal):

    def __init__(self,species,name):
        super().__init__(species,name)
    
    def bask_in_sun(self):
        return (f"{self.name} the {self.species} is basking in the sun")

# ------------------ MAMMAL CLASS ------------------

class Primate(Mammal):

    def __init__(self,name,species):
        super().__init__(species,name)
    
    def climb_trees(self):
        return (f"{self.name} the {self.species} is climbing trees")

# ------------------ MARSUPIAL CLASS --------------
        
class Marsupial(Mammal):

    def __init__(self, name, species):
        super().__init__(species,name)

    def carry_baby(self):
        return (f"{self.name} the {self.species} is carrying its baby")

# ------------------ AVIARY CLASS ------------------
        
class Aviary():

    def __init__(self,birds =[]):
        self.birds = birds
    

# ------------------ REPTILE CLASS ------------------

class ReptileEnclosure():

    def __init__(self,reptiles = []):
        self.reptiles = reptiles   
