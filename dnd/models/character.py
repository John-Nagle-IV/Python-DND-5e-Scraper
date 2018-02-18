import copy
import json

from dnd.models.constants import *


class BaseModel(object):
    export = []
    @classmethod
    def from_json(cls, json_str):
        return cls.from_dict(json.loads(json_str))

    def from_dict(cls, dic):
        return cls(**dic)

    def __init__(self, *args, **kwargs):
        for index, arg in enumerate(args):
            try:
                setattr(self, export[index], arg)
            except IndexError:
                raise
        for attr, val in kwargs.items():
            if attr in self.export:
                setattr(self, attr, val)

    def __dict__(self):
        return {attr:getattr(self, attr, None) for attr in self.export}

    def serialize(self):
        return json.dumps(self.__dict__())


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
        result.max_speed = min(filter(None, {self.max_speed, other.max_speed}))
        result.max_dex = min(filter(None, {self.max_dex, other.max_dex}))
        return result


class God(object):
    def __init__(
        self,
        name='',
        description='',
        alignment='',
        domain=None,
        symbol='',
        source='',
        table=''
    ):
        self.name = name
        self.description = description
        self.alignment = alignment
        self.domain = domain or []
        self.symbol = symbol
        self.source = source
        self.table = table



class Race(object):
    def __init__(self):
        super(Race, self).__init__()
        self.size = Sizes.MEDIUM
        self.ability_score_bonus = AbilityScore()
        self.age = 0
        self.alignment = Alignment.NEUTRAL
        self.speed = 30


class AbilityScore(object):
    @classmethod
    def from_dict(cls, dict_obj):
        return cls(
            dict_obj.get('STR', 0),
            dict_obj.get('DEX', 0),
            dict_obj.get('CON', 0),
            dict_obj.get('WIS', 0),
            dict_obj.get('INT', 0),
            dict_obj.get('CHA', 0)
        )

    def __init__(self, stren=0, dex=0, con=0, wis=0, intel=0, cha=0):
        super(AbilityScore, self).__init__()
        self.STR = stren
        self.DEX = dex
        self.CON = con
        self.WIS = wis
        self.INT = intel
        self.CHA = cha

    def __dict__(self):
        return {
            'STR': self.STR,
            'DEX': self.DEX,
            'CON': self.CON,
            'WIS': self.WIS,
            'INT': self.INT,
            'CHA': self.CHA,
        }

    def __radd__(self, other):
        other = int(other)
        return AbilityScore(
            self.STR + other,
            self.DEX + other,
            self.CON + other,
            self.WIS + other,
            self.INT + other,
            self.CHA + other
        )


    def __add__(self, other):
        return AbilityScore(
            self.STR + other.STR,
            self.DEX + other.DEX,
            self.CON + other.CON,
            self.WIS + other.WIS,
            self.INT + other.INT,
            self.CHA + other.CHA
        )

    def __sub__(self, other):
        return AbilityScore(
            self.STR - other.STR,
            self.DEX - other.DEX,
            self.CON - other.CON,
            self.WIS - other.WIS,
            self.INT - other.INT,
            self.CHA - other.CHA
        )

    def __rsub__(self, other):
        other = int(other)
        return AbilityScore(
            self.STR - other,
            self.DEX - other,
            self.CON - other,
            self.WIS - other,
            self.INT - other,
            self.CHA - other
        )

    def __copy__(self):
        return AbilityScore(
            self.STR,
            self.DEX,
            self.CON,
            self.WIS,
            self.INT,
            self.CHA
        )


class Character(object):
    def __init__(self):
        super(Character, self).__init__()
        self._race = Race()
        self._base_attributes = AbilityScore()
        self._health = 0
        self._max_health = 0
        self._character_name = ""
        self._game_class = []
        self._alignment = alignment.NEUTRAL
        self._deity = gods.God()
        self._equipment_list = []

    @property
    def max_health(self):
        return self._max_health

    @property
    def health(self):
        return self._health

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
            int((self.attributes.STR - 10) / 2),
            int((self.attributes.DEX - 10) / 2),
            int((self.attributes.CON - 10) / 2),
            int((self.attributes.WIS - 10) / 2),
            int((self.attributes.INT - 10) / 2),
            int((self.attributes.CHA - 10) / 2)
        )

    @property
    def armor_class(self):
        max_dex_equipment = None
        ac_bonus_equipment = 0
        for e in self.equipment_list:
            if max_dex_equipment is None or e.max_dex < max_dex_equipment:
                max_dex_equipment = e.max_dex
            ac_bonus_equipment += e.ac_bonus
        return 10 + min(filter(None, {self.mod.DEX, max_dex_equipment})) + ac_bonus_equipment

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
        return min(
            filter(None, {self.race.speed,
                filter(None, set(e.max_speed for e in self.equipment_list))}
            )
        )

    @property
    def equipment_list(self):
        return self._equipment_list
