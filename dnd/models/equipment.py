from abilityscore import AbilityScore
from ..utils import min_no_none

class Equipment(object):
    def __init__(self):
        super(Equipment, self).__init__()
        self.ability_score_bonus = AbilityScore()
        self.ac_bonus = 0
        self.name = ""
        self.effect = ""
        self.max_speed = None
        self.max_dex = None

    def __add__(self, other):
        result = Equipment()
        result.ac_bonus = self.ac_bonus + other.ac_bonus
        result.ability_score_bonus = self.ability_score_bonus + other.ability_score_bonus
        result.max_speed = min_no_none({self.max_speed, other.max_speed})
        result.max_dex = min_no_none({self.max_dex, other.max_dex})
        return result
