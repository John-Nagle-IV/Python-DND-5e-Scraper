from abilityscore import AbilityScore
from constants import *


class Race(object):
    def __init__(self):
        super(Race, self).__init__()
        self.size = Sizes.MEDIUM
        self.ability_score_bonus = AbilityScore()
        self.age = 0
        self.alignment = Alignment.NEUTRAL
        self.speed = 30

