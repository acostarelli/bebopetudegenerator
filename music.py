import math
from enum import Enum

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

    def __eq__(self, t):
        return self.__note == t.__note and self.__rhythm == t.__rhythm

class Rest:
    def __gt__(self, t):
        return True

    def __lt__(self, t):
        return True

    def __eq__(self, t):
        return True

    def __add__(self, t):
        return self

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
"""class Quality:
    M   = 0
    dom = 1
    m   = 2
    pu  = 3"""

class Quality(Enum):
    M   = (Note.III, Note.V, Note.VII)
    dom = (Note.III, Note.V, Note.bVII)
    m   = (Note.bIII, Note.V, Note.bVII)
    pu  = (0, 0, 0)

    def __init__(self, third, fifth, seventh):
        self.__third = third
        self.__fifth = fifth
        self.__seventh = seventh

    @property
    def third(self):
        return self.__third

    @property
    def fifth(self):
        return self.__fifth

    @property
    def seventh(self):
        return self.__seventh

    def __eq__(self, t):
        return self.third == t.third and self.fifth == t.fifth and self.seventh == t.seventh

    def __iter__(self):
        yield self.__third
        yield self.__fifth
        yield self.__seventh

    def __contains__(self, t):
        return t == self.third or t == self.fifth or t == self.seventh

    def __str__(self):
        return f"({self.third},{self.fifth},{self.seventh})"


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