class GameClass(object):
    def __init__(self):
        self._class_name = ''
        self._class_level = 1
        self._class_abilities = []

    @property
    def class_name(self):
        return self._class_name

    @property
    def class_level(self):
        return self._class_level

    @property
    def class_abilities(self):
        return self._class_abilities
