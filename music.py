import math

class Event:
    def __init__(self, note, rhythm):
        self.__note   = note
        self.__rhythm = rhythm

    @property
    def note(self):
        return self.__note

    @property
    def rhythm(self):
        return self.__rhythm

    def __str__(self):
        return f"{str(self.__note)} {str(self.__rhythm)}"

class Note:
    I   = 0
    bII = 1
    II  = 2
    bIII = 3
    III = 4
    IV  = 5
    bV  = 6
    V   = 7
    bVI = 8
    VI  = 9
    bVII = 10
    VII = 11
    REST = math.inf

class Rhythm:
    Q = 12
    E = 6
    T = 4
    S = 3

# can make this a fancy enum
class Quality:
    M   = 0
    dom = 1
    m   = 2
    pu  = 3

class Chord:
    def __init__(self, quality, root):
        self.__quality = quality
        self.__root    = root

    @property
    def quality(self):
        return self.__quality

    @property
    def root(self):
        return self.__root