import math


class Weapon:
    def __init__(self, name="", damage=10):
        self.__name = name
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, damage):
        if damage in range(0, 100):
            self.__damage = damage
        else:
            print("Недопустимый урон оружия")

    def __le__(self, other):
        return self.damage <= other.damage
