"""
- maybe two types of nodes: note modification and lick selection
- instrument range
- less chromaticism
"""

class Solo:
    """
    stores the state for a generating solo
    """
    def __init__(self):
        pass

class CatNode:
    def __init__(self):
        pass

    def __call__(self):
        pass

class OctaveCorrection(CatNode):
    def __call__(self, solo):
        pass

class Cat(list):
    def __init__(self, licks, nodes):
        super().__init__(nodes)
        self.__licks = licks

    def __call__(self, chords):
        for chord in chords:
            pass
