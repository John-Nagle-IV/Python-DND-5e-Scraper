class AbilityScore(object):
    def __init__(self):
        super(AbilityScore, self).__init__()
        self.STR = 0
        self.DEX = 0
        self.CON = 0
        self.WIS = 0
        self.INT = 0

    def __add__(self, other):
        new_score = AbilityScore()
        new_score.STR = self.STR + other.STR
        new_score.DEX = self.DEX + other.DEX
        new_score.CON = self.CON + other.CON
        new_score.WIS = self.WIS + other.WIS
        new_score.INT = self.INT + other.INT
        return new_score

    def __sub__(self, other):
        new_score = AbilityScore()
        new_score.STR = self.STR - other.STR
        new_score.DEX = self.DEX - other.DEX
        new_score.CON = self.CON - other.CON
        new_score.WIS = self.WIS - other.WIS
        new_score.INT = self.INT - other.INT
        return new_score
