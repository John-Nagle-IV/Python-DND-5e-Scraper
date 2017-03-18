import alignment
import gods

from abilityscore import AbilityScore
from races import Race

class Character(object):
    def __init__(self):
        super(Character, self).__init__()
        self.race = Race()
        self.attributes = AbilityScore()
        self.mod = AbilityScore()
        self.AC = 0
        self.health = 0
        self.name = ""
        self.game_class = {} # TODO Game classes data obj
        self.alignment = alignment.NEUTRAL
        self.deity = gods.God()
        self.speed = 0
        self.equipment_list = []
        # Update to fill in calculated values
        self.update()

    def update(self):
        self.mod = self.calc_ablility_score_mod()
        self.AC = self.calc_armor_class()
        self.speed = self.calc_speed()

    def calc_speed(self):
        return self.race.speed

    def calc_armor_class(self):
        return 10 + self.mod.DEX # + armor + other

    def calc_ablility_score_mod(self):
        mod = AbilityScore()
        mod = self.race.ability_score_bonus + self.attributes
        mod.STR = (mod.STR - 10) / 2
        mod.DEX = (mod.DEX - 10) / 2
        mod.CON = (mod.CON - 10) / 2
        mod.WIS = (mod.WIS - 10) / 2
        mod.INT = (mod.INT - 10) / 2
        return mod

