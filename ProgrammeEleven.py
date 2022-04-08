#programme to fing the total number of legs of farm animals
#Approach One: Using class
class FarmAnimal:
    def __init__(self, chicken, cows, pigs):
        self.chicken = chicken
        self.cows = cows
        self.pigs = pigs

    def count_legs(self):
        #Chicken has 2 legs, Cows have Four legs and Pigs have 2 legs
        ch = self.chicken * 2
        c = self.cows * 4
        p = self.pigs * 4
        legs = ch + c + p
        return legs

mcdonell_farm = FarmAnimal(7, 11, 5)
print(mcdonell_farm.count_legs())

