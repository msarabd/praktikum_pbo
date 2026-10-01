class Hero:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def serang(self, target):
        print(f"{self.name} menyerang {target.name}")

class Mage(Hero):
    def __init__(self, name, health, attack, mana=100):
        super().__init__(name, health, attack)
        self.mana = mana

    def serang(self, target):
        print(f"{self.name} menyerang musuh dengan magis {target.name}")

class Assasin(Hero):
    def __init__(self, name, health, attack, mana=100):
        super().__init__(name, health, attack)
        self.mana = mana

class DoubleRole(Mage, Assasin):
    def __init__(self, name, health, attack, mana, jarak):
        super().__init__(name, health, attack, mana)
        self.jarak = jarak

    def serang(self, target):
        if self.jarak < 50:
            print(f"error")
        else:
            print(f"{self.name} berhasil menyerang {target.name} dengan jarak {self.jarak}")

        
class AssasinEnergy(Assasin):
    def __init__(self, name, health, attack, mana, energy):
        super().__init__(name, health, attack, mana)
        self.energy = energy

    def serang(self, target):
        print(f"{self.name} menyerang {target.name} ")

balmond = Mage("Balmond", 1000, 10, 2000)
eudora = Mage("Eudora", 1000, 12, 2000)
balmond.serang(eudora)

fanny = AssasinEnergy("Fanny", 1000, 10, 2000, 3000)
fanny.serang(balmond)

yss = DoubleRole("YSS", 1000, 40, 2000, 200)
yss.serang(fanny)
# print(help(yss))