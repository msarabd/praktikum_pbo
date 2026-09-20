class Kicker():
    __jumlahKicker = 0

    def __init__(self, name, team, shotStat=0):
        self.name = name
        self.__team = team
        self.__shotStat = shotStat
        Kicker.__jumlahKicker += 1

    @property
    def team(self):
        return self.__team

    @team.setter
    def team(self, value):
        if value.lower() == "barca" or value.lower() == "madrid":
            self.__team = value.lower()
        else:
            raise ValueError

    @property
    def shotStat(self):
        return self.__shotStat

    @shotStat.setter
    def shotStat(self, value):
        if not isinstance(value, int):
            raise TypeError
        if value >= 0:
            self.__shotStat = value
        else:
            raise ValueError

    @staticmethod
    def get_JumlahKicker():
        return Kicker.__jumlahKicker

class Keeper():
    __jumlahKeeper = 0
    
    def __init__(self, name, team, reachStat=0):
        self.name = name
        self.__team = team
        self.__reachStat = reachStat
        Keeper.__jumlahKeeper += 1

    @property
    def team(self):
        return self.__team

    @team.setter
    def team(self, value):
        if value.lower() == "barca" or value.lower() == "madrid":
            self.__team = value.lower()
        else:
            raise ValueError

    @property
    def reachStat(self):
        return self.__reachStat

    @reachStat.setter
    def reachStat(self, value):
        if not isinstance(value, int):
            raise TypeError
        if value >= 0:
            self.__reachStat = value
        else:
            raise ValueError

    @staticmethod
    def get_JumlahKeeper():
        return Keeper.__jumlahKeeper

class Match():
    __jumlahMatch = 0
    
    def __init__(self, skorA=0, skorB=0):
        self.__skorA = skorA
        self.__skorB = skorB
        self.__jumlahPutaran = skorA + skorB
        Match.__jumlahMatch += 1
        
    @property
    def jumlahPutaran(self):
        return self.__jumlahPutaran

    @classmethod
    def show_jumlahMatch(cls):
        print(f"Kedua tim sudah bertemu {cls.__jumlahMatch} kali pertandingan")

    @jumlahPutaran.setter
    def jumlahPutaran(self, value):
        if not isinstance(value, int):
            raise TypeError
        if value > 5:
            self.__jumlahPutaran = value % 5
        elif value < 0:
            raise ValueError
        else:
            self.__jumlahPutaran = value
    
    def add_goal(self, team):
        if team ==  "barca":
            self.__skorA += 1
        elif team == "madrid":
            self.__skorB += 1
        else:
            raise ValueError
        self.__jumlahPutaran += 1
        
    def get_skor(self):
        return "Skor: {} - {}".format(self.__skorA,self.__skorB)

kicker1 = Kicker("Andi", "Barca", 23)
kicker2 = Kicker("Budi", "madrid", 88)
keeper1 = Keeper("Anton", "maDRID", 75)
keeper2 = Keeper("Beni", "BARCA", 80)
match1 = Match(0, 0)
match2 = Match(3, 2)

print(Kicker.get_JumlahKicker())
print(Keeper.get_JumlahKeeper())

match1.add_goal("barca")
print(match1.jumlahPutaran)
print()

print(match2.jumlahPutaran)
print(match2.get_skor())
match2.add_goal("barca")
print(match2.jumlahPutaran)
print(match2.get_skor())
Match.show_jumlahMatch()
print()

print(kicker1.team)
kicker1.team = "madrid"
print(kicker1.team)

print(kicker2.shotStat)
kicker2.shotStat = 23
print(kicker2.shotStat)

print(keeper1.team)
keeper1.team = "BARCA"
print(keeper1.team)

print(keeper2.reachStat)
keeper2.reachStat = 100
print(keeper2.reachStat)

print(match1.jumlahPutaran)
match1.jumlahPutaran = 7
print(match1.jumlahPutaran)
print()

# kicker1.team = "chelsea" 
# kicker2.shotStat = -5
# keeper1.team = ""
# keeper2.reachStat = "ty"
# match2.jumlahPutaran = ""
