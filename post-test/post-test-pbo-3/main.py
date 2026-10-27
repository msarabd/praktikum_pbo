import os
import random
from abc import ABC, abstractmethod

class Player(ABC):
    __playerCount = 0

    def __init__(self, name, team=None):
        self._name = name
        self._team = team
        self.respawn()
        Player.__playerCount += 1

    @property
    def name(self):
        return self._name

    @property
    def team(self):
        return self._team

    @team.setter
    def team(self, value):
        self._team = value

    @classmethod
    def get_player_count(cls):
        return cls.__playerCount

    @abstractmethod
    def perform_action(self):
        pass

    @abstractmethod
    def get_effective_stat(self):
        pass
    
    def respawn(self):
        print(f"Berhasil menambah pemain atas nama {self._name}")

    def show_profile(self):
        if self._team:
            team_name = self._team
        else:
            team_name = "Tanpa tim"
        print(f"[{self.__class__.__name__}] Nama: {self._name} | Tim: {team_name}")

    def __gt__(self, other):
        if not isinstance(other, Player):
            return NotImplemented
        return self.get_effective_stat() > other.get_effective_stat()

    def __str__(self):
        return f"[{self.__class__.__name__}] {self._name} (Stat: {self.get_effective_stat()})"
    
class Team:
    __teamCount = 0

    def __init__(self, name):
        self._name = name
        self._players = []
        self.respawn()
        Team.__teamCount += 1

    @property
    def name(self):
        return self._name

    @property
    def players(self):
        return self._players

    @classmethod
    def get_teamCount(cls):
        return cls.__teamCount

    def add_player(self, player):
        self._players.append(player)
        player.team = self
        print(f"Berhasil menambah {player.name} ke dalam tim {self._name}")

    def respawn(self):
        print(f"Berhasil menambah tim {self._name}")

    def __str__(self):
        return f"Tim {self._name}"

class Kicker(Player):
    __kickerCount = 0

    def __init__(self, name, team=None, shotStat=0):
        super().__init__(name, team)
        self.__shotStat = max(0, shotStat)
        Kicker.__kickerCount += 1

    @property
    def shotStat(self):
        return self.__shotStat

    @shotStat.setter
    def shotStat(self, value):
        if not isinstance(value, int):
            raise TypeError("shotStat harus berupa integer")
        if value < 0:
            raise ValueError("shotStat tidak boleh negatif")
        self.__shotStat = value

    @classmethod
    def get_kickerCount(cls):
        return cls.__kickerCount

    def perform_action(self):
        return f"{self._name} melepaskan tembakan terarah dengan daya {self.__shotStat}!"

    def get_effective_stat(self):
        return self.__shotStat

    def respawn(self):
        print(f"Berhasil menambah penendang atas nama {self._name}")

class Keeper(Player):
    __keeperCount = 0

    def __init__(self, name, team=None, reachStat=0):
        super().__init__(name, team)
        self.__reachStat = max(0, reachStat)
        Keeper.__keeperCount += 1

    @property
    def reachStat(self):
        return self.__reachStat

    @reachStat.setter
    def reachStat(self, value):
        if not isinstance(value, int):
            raise TypeError("reachStat harus berupa integer")
        if value < 0:
            raise ValueError("reachStat tidak boleh negatif")
        self.__reachStat = value

    @classmethod
    def get_keeperCount(cls):
        return cls.__keeperCount

    def perform_action(self):
        return f"{self._name} melompat meregangkan badan menjangkau bola (Jangkauan: {self.__reachStat})!"

    def get_effective_stat(self):
        return self.__reachStat
    
    def respawn(self):
        print(f"Berhasil menambah kiper atas nama {self._name}")

class MatchRound:
    DIRECTIONS = ("kiri", "tengah", "kanan")

    def __init__(self, round_no, kicker, keeper, kicker_dir=None, keeper_dir=None):
        self._round_no = round_no
        self._kicker = kicker
        self._keeper = keeper
        self._kicker_dir = kicker_dir if kicker_dir in self.DIRECTIONS else random.choice(self.DIRECTIONS)
        self._keeper_dir = keeper_dir if keeper_dir in self.DIRECTIONS else random.choice(self.DIRECTIONS)
        self._result, self._is_goal = self.__execute_duel()

    def __execute_duel(self):
        if random.random() < 0.05:
            return "Tendangan Melebar!", False

        if self._kicker_dir != self._keeper_dir:
            return "GOL! Kiper salah membaca arah bola!", True

        power_shot = self._kicker.shotStat + random.randint(1, 15)
        reach_save = self._keeper.reachStat + random.randint(1, 15)

        if power_shot > reach_save:
            return "GOL! Tembakan terlalu keras meski arah terbaca!", True
        else:
            return "DITEPIS! Kiper melakukan penyelamatan yang sangat brilian!", False

    @property
    def is_goal(self):
        return self._is_goal

    @property
    def scoring_team(self):
        if self._is_goal:
            return self._kicker.team
        return None

    def get_log(self):
        team_kicker_name = self._kicker.team.name if self._kicker.team else "Tanpa Tim"
        team_keeper_name = self._keeper.team.name if self._keeper.team else "Tanpa Tim"

        return (f"""\n[Putaran {self._round_no}]\n
{self._kicker.name} ({team_kicker_name}) menembak ke {self._kicker_dir} |
{self._keeper.name} ({team_keeper_name}) melompat ke {self._keeper_dir}\n
-> {self._result}""")


class Match:
    def __init__(self, teamA, teamB):
        self._teamA = teamA
        self._teamB = teamB
        self._score = {teamA: 0, teamB: 0}
        self._rounds = []

    @property
    def score(self):
        return {team.name: pts for team, pts in self._score.items()}

    def add_round(self, kicker, keeper, kicker_dir=None, keeper_dir=None):
        round_no = len(self._rounds) + 1
        currentRound = MatchRound(round_no, kicker, keeper, kicker_dir, keeper_dir)
        self._rounds.append(currentRound)

        if currentRound.is_goal and currentRound.scoring_team in self._score:
            self._score[currentRound.scoring_team] += 1

        print(currentRound.get_log())

    def show_history(self):
        print("\n=== Histori Putaran Penalti ===")
        for r in self._rounds:
            print(r.get_log())

def initiate_match(participant):
    participant.respawn()

os.system("cls")
print("=== 1. ABSTRAKSI ===")
try:
    dummy = Player("Pemain Abstrak")
except TypeError as err:
    print(f"Berhasil membuktikan kegagalan instansiasi ABC: {err}\n")

team1 = Team("Barcelona")
team2 = Team("Madrid")

kicker1 = Kicker("Baker", shotStat=80)
kicker2 = Kicker("Chanatip", shotStat=75)
print()

keeper1 = Keeper("Emil", reachStat=85)
keeper2 = Keeper("Paes", reachStat=70)
print()

team1.add_player(kicker1)
team1.add_player(keeper1)

team2.add_player(kicker2)
team2.add_player(keeper2)
print()

print(f"=== 2. METHOD KONKRET BERSAMA DARI ABSTRACT CLASS ===")
kicker1.show_profile()
keeper1.show_profile()
print()

print(f"=== 3. POLIMORPISME ===")
player_list = [kicker1, keeper2]
for i in player_list:
    print(i.perform_action())
print()

print(f"=== 4. DUCK TYPING ===")
initiate_match(kicker2)
initiate_match(team2)
print()

print(f"=== 5. OPERATOR OVERLOADING ===")
print(kicker1)
print(keeper1)
if kicker1 > keeper2:
    print(f"Stat {kicker1._name} lebih besar dari pada stat {keeper2}")
else:
    print(f"Stat {kicker1._name} lebih kecil dari pada stat {keeper2}")
print()

print("=== 6. SIMULASI PERTANDINGAN (KOMPOSISI & ASOSIASI) ===")
match_final = Match(team1, team2)
match_final.add_round(kicker=kicker1, keeper=keeper2, kicker_dir="kanan", keeper_dir="kanan")
match_final.add_round(kicker=kicker2, keeper=keeper1, kicker_dir="kiri", keeper_dir="tengah")
print(f"\nSkor Akhir: {match_final.score}")