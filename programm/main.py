from programm.warrior import Warrior
from programm.bow import Bow
from programm.sword import Sword
import random
import copy



def best_weapons(list):
    best_weapons_index = 0
    for i in range(len(list) - 1):
        if (list[i].__le__(list[i + 1])):
            best_weapons_index = i + 1
    return best_weapons_index


def start_game():
    warrior1 = Warrior("Воин1")
    warrior2 = Warrior("Воин2")
    warrior3 = Warrior("Воин3")
    list_warrior = [warrior1, warrior2, warrior3]
    gameStatus = True
    copy_list_warrior = []
    while gameStatus:
        first = random.randint(0, len(list_warrior) - 1)
        second = random.randint(0, len(list_warrior) - 1)
        while second == first:
            second = random.randint(0, len(list_warrior) - 1)
        list_warrior[second].health -= list_warrior[first].damage
        copy_list_warrior = copy.copy(list_warrior)
        for i in range(len(copy_list_warrior)):
            if (copy_list_warrior[i].health <= 0):
                list_warrior[i].__del__()
                del list_warrior[i]
        if (len(list_warrior) == 1):
            gameStatus = False
    print("Победитель!!!")
    list_warrior[0].printInformation()
    list_weapons = []
    bow1 = Bow("Лук1", 9, 85)
    bow2 = Bow("Лук2",100, 68)
    sword = Sword("Меч1", 102, 100)
    list_weapons.append(bow1)
    list_weapons.append(bow2)
    list_weapons.append(sword)
    a = best_weapons(list_weapons)
    print(list_weapons[a].name)




 