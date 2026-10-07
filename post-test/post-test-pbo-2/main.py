import os
import random

class Player:
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

    def respawn(self):
        print(f"Berhasil menambah pemain atas nama {self._name}")


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
        if value >= 0:
            self.__shotStat = value
        else:
            raise ValueError("shotStat tidak boleh negatif")

    @classmethod
    def get_kickerCount(cls):
        return cls.__kickerCount

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
        if value >= 0:
            self.__reachStat = value
        else:
            raise ValueError("reachStat tidak boleh negatif")

    @classmethod
    def get_keeperCount(cls):
        return cls.__keeperCount

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
    def is_goal(self) -> bool:
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

os.system("cls")
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
print(f"Total Pemain Terbuat : {Player.get_player_count()}")
print(f"Total Tim Terbuat    : {Team.get_teamCount()}")
print(f"Total Kicker Terbuat : {Kicker.get_kickerCount()}")
print(f"Total Keeper Terbuat : {Keeper.get_keeperCount()}")

kicker1.shotStat = 85
print(f"Stat tembakan {kicker1.name} diperbarui menjadi: {kicker1.shotStat}")

match_final = Match(team1, team2)

match_final.add_round(
    kicker=kicker1, 
    keeper=keeper2, 
    kicker_dir="kanan", 
    keeper_dir="kanan"
)

match_final.add_round(
    kicker=kicker2, 
    keeper=keeper1, 
    kicker_dir="kiri", 
    keeper_dir="tengah"
)

print(f"\nSkor Akhir: {match_final.score}")