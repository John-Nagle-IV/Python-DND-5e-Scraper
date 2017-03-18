from abilityscore import AbilityScore

class Equipment(object):
    def __init__(self):
        super(Equipment, self).__init__()
        self.ability_score_bonus = AbilityScore()
        self.ac_bonus = 0
        self.name = ""
        self.effect = ""
        self.max_speed = 30
        self.max_dex = 100

    def __add__(self, other):
        result = Equipment()
        result.ac_bonus = self.ac_bonus + other.ac_bonus
        result.ability_score_bonus = self.ability_score_bonus + other.ability_score_bonus
        result.max_speed = self.max_speed if self.max_speed < other.max_speed else other.max_speed
        result.max_dex = self.max_dex if self.max_dex < other.max_dex else other.max_dex
        return result

