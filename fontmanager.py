# manage fonts

import copy

class Font:
    def __init__(self, family):
        self.family = family

class FontManager(object):
    __instance = None

    _fonts = {}

    def __new__(cls):
        if FontManager.__instance is None:
            FontManager.__instance = object.__new__(cls)
        return FontManager.__instance

    def _loadFont(self, family):
        return Font(family)

    def getFont(self, family):
        if self._fonts.get(family) == None:
            self._fonts[family] = self._loadFont(family)

        return self._fonts[family]
