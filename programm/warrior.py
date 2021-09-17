class Warrior:
    def __init__(self, name="Warrior", health=100, damage=20):
        self.name = name
        self.health = health
        self.damage = damage

    def printInformation(self):
        print(f"Воин {self.name} имеет {self.health} здоровья и имеет {self.damage} урона.")

    def __del__(self):
        print(f"Valhalla, {self.name} is coming.")
