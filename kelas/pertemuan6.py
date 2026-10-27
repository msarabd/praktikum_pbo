class Hero: # hanya pertarungan
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def serang(self, target):
        target.health -= 10

class TampilanHero: # hanya tampilan
    def tampilkan(self, hero):
        print(f"{hero.name} | HP {hero.health}")

class PenyimpanHero: # hanya penyimpanan
    def simpan(self, hero, nama_file):
        with open(nama_file, "a") as f:
            f.write(f"{hero.name},{hero.health}\n")

layla = Hero("Layla", 70)
Hero("Balmond", 120).serang(layla)
TampilanHero().tampilkan(layla)
PenyimpanHero().simpan(layla, "data_hero.txt")

def hitung_damage(role, attack):
    if role == "fighter":
        return attack + 5
    elif role == "mage":
        return attack * 2
    # role baru = ubah fungsi ini lagi
    return 0

print(hitung_damage("fighter", 10))
print(hitung_damage("mage", 10))
print(hitung_damage("assassin", 10))

class Hero:
    def __init__(self, attack):
        self.attack = attack
    
    def hitung_damage(self):
        return self.attack

class Fighter(Hero):
    def hitung_damage(self):
        return self.attack + 5

class Mage(Hero):
    def hitung_damage(self):
        return self.attack * 2

class Assassin(Hero): # role baru: cukup tambah kelas
    def hitung_damage(self):
        return self.attack * 3

print(Fighter(10).hitung_damage())
print(Mage(10).hitung_damage())
print(Assassin(10).hitung_damage())

class Unit:
    def bergerak(self):
        print("Unit bergerak")

class Minion(Unit):
    pass

class Turret(Unit):
    def bergerak(self): # melanggar janji parent
        raise Exception("Turret tidak bisa bergerak!")

def maju(unit: Unit):
    unit.bergerak()

maju(Minion())
# maju(Turret())

class Unit:
    pass # hanya yang dimiliki semua unit

class UnitBergerak(Unit):
    def bergerak(self):
        print("Unit bergerak")

class Minion(UnitBergerak):
    pass

class Turret(Unit): # tidak berjanji bisa bergerak
    def tembak(self):
        print("Turret menembak")

def maju(unit: UnitBergerak):
    unit.bergerak()

maju(Minion())
Turret().tembak()