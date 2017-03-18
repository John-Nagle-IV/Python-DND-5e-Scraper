from abilityscore import AbilityScore
import alignment


class Race(object):
    def __init__(self):
        super(Race, self).__init__()
        self.size = 'M'
        self.ability_score_bonus = AbilityScore()
        self.age = 0
        self.alignment = alignment.NEUTRAL
        self.speed = 30

