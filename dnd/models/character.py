import alignment
import copy
import gods

from equipment import Equipment
from abilityscore import AbilityScore
from races import Race
from ..utils import min_no_none

class Character(object):
    def __init__(self):
        super(Character, self).__init__()
        self._race = Race()
        self._base_attributes = AbilityScore()
        self._health = 0
        self._character_name = ""
        self._game_class = []
        self._alignment = alignment.NEUTRAL
        self._deity = gods.God()
        self._equipment_list = []

    @property
    def character_level(self):
        return sum([cl.class_level for cl in self.game_class])

    @property
    def race(self):
        return self._race

    @property
    def attributes(self):
        equipment_ability_bonus = AbilityScore()
        for e in self.equipment_list:
            equipment_ability_bonus = e.ability_score_bonus + equipment_ability_bonus
        return self._base_attributes + self.race.ability_score_bonus + equipment_ability_bonus

    @property
    def mod(self):
        return AbilityScore(
            (self.attributes.STR - 10) / 2,
            (self.attributes.DEX - 10) / 2,
            (self.attributes.CON - 10) / 2,
            (self.attributes.WIS - 10) / 2,
            (self.attributes.INT - 10) / 2,
            (self.attributes.CHA - 10) / 2
        )

    @property
    def armor_class(self):
        max_dex_equipment = None
        ac_bonus_equipment = 0
        for e in self.equipment_list:
            if max_dex_equipment is None or e.max_dex < max_dex_equipment:
                max_dex_equipment = e.max_dex
                ac_bonus_equipment += e.ac_bonus
        return 10 + min_no_none({self.mod.DEX, max_dex_equipment}) + ac_bonus_equipment

    @property
    def health(self):
        return self._health

    @property
    def character_name(self):
        return self._character_name

    @property
    def game_class(self):
        return self._game_class

    @property
    def alignment(self):
        return self._alignment

    @property
    def deity(self):
        return self._deity

    @property
    def speed(self):
        return min_no_none({self.race.speed, min_no_none(set(e.max_speed for e in self.equipment_list))})

    @property
    def equipment_list(self):
        return self._equipment_list
