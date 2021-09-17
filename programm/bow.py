from programm.weapon import Weapon
import random


class Bow(Weapon):

    def __init__(self, name="Лук", damage=10, chance=60):
        self.__name = name
        self.__damage = damage
        self.__chance = chance

    @property
    def name(self):
        return self.__name

    @property
    def chance(self):
        return self.__chance

    def potential_damage(self):
        return self.__damage * (self.__chance * 0.01)

    def attack(self):
        chance_attack = self.__chance * 0.01
        rn = random.random()
        if rn <= chance_attack:
            return self.__damage
        else:
            return 0

    @property
    def damage(self):
        return self.potential_damage()
