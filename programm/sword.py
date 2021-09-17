from programm.weapon import Weapon
import random


class Sword(Weapon):

    def __init__(self, name="Меч", damage=10, durability=100):
        self.__name = name
        self.__damage = damage
        self.__durability = durability

    @property
    def name(self):
        return self.__name

    def attack(self):
        attack_damage = self.__damage * (self.__durability * 0.01)
        if random.randint(0, 1) == 0:
            if self.__durability == 0:
                return 0
            else:
                self.__durability -= 10
        return attack_damage

    @property
    def damage(self):
        return self.attack()
