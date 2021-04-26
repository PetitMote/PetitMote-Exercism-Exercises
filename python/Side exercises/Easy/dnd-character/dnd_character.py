from random import randint

def modifier(constitution):
    constitution_modifier = (constitution - 10) // 2
    return constitution_modifier

class Character:

    def __init__(self):
        self.strength = self.carac_roll()
        self.dexterity = self.carac_roll()
        self.constitution = self.carac_roll()
        self.intelligence = self.carac_roll()
        self.wisdom = self.carac_roll()
        self.charisma = self.carac_roll()
        self.hitpoints = 10 + modifier(self.constitution)

    @staticmethod
    def carac_roll():
        dices = (randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6))
        carac = sum(dices) - min(dices)
        return carac

    def ability(self):
        abilities = (self.strength, self.dexterity, self.constitution, self.intelligence, self.wisdom, self.charisma)
        return abilities[randint(0, 5)]

