"""
- maybe two types of nodes: note modification and lick selection
- instrument range
- less chromaticism
"""

class Cat:
    def __init__(self):
        pass

    def __iter__(self):
        while True:
            yield next(lick in self.licks if self.__licks

class DavidBaker(Cat):
    def __weight(self, lick, last, chord):
        weight = 0

        if lick.quality != chord.quality:
            return 0

        diff = abs((last % 12) - (chord.root + lick.first.note) % 12)
        #[abs(((tone + chord.root) % 12) - (last % 12)) for tone in chord.quality]
        diff = diff - (12 * (diff // 6))
        if diff == 1: # this is flawed... licks that aren't 1 away will get away with this
        # you want to say: if the last note is a half step away from a chord tone, choose licks that start on that chord tone
            if lick.first.note in chord.quality:
                return 1
            else:
                return 0
            #return 1
        elif diff in [2, 3]:
            return 1

        return 0

    def __licks(self):
        pass

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
