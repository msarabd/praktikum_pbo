class Hero:
    mobil = 2000

    def __init__(a, name):
        a.name = name 

    @classmethod
    def getInfo1(cls):
        return cls.mobil

    @staticmethod
    def getInfo2():
        return Hero.mobil

andi = Hero("andi")
print(Hero.getInfo2())