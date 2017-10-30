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
