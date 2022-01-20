from music import Quality, Event, Note, Rhythm

class Lick:
    def __init__(self, quality, *events):
        self.__quality = quality
        self.__events  = events

    @property
    def quality(self):
        return self.__quality

    @property
    def first(self):
        return next(event for event in self.__events if event.note != Note.REST)

    @property
    def last(self):
        return next(event for event in reversed(self.__events) if event.note != Note.REST)

    def __getitem__(self, i):
        return self.__events[i]

    def __iter__(self):
        for event in self.__events:
            yield event

    def __eq__(self, t):
        return self.__quality == t.__quality and self.__events == t.__events

    def __len__(self):
        return len(self.__events)

licks = [
    Lick(Quality.m, # 1.1
        Event(Note.I, Rhythm.E), Event(-1, Rhythm.E),
        Event(0, Rhythm.E), Event(2, Rhythm.E)),
    Lick(Quality.m, # 1.1
        Event(Note.bIII, Rhythm.E), Event(2, Rhythm.E),
        Event(4, Rhythm.E), Event(7, Rhythm.E)),
    Lick(Quality.dom, # 1.1
        Event(Note.VI, Rhythm.E), Event(1, Rhythm.E),
        Event(0, Rhythm.E), Event(-2, Rhythm.E)),
    Lick(Quality.dom, # 1.1
        Event(Note.bV, Rhythm.E), Event(-2, Rhythm.E),
        Event(-3, Rhythm.E), Event(-5, Rhythm.E)),
    #Lick(Quality.M, # 1.1
    #    Event(Note.V, Rhythm.Q), Event(Note.REST, Rhythm.Q)),
    Lick(Quality.m, # 1.2
        Event(Note.bIII, Rhythm.E), Event(-1, Rhythm.E),
        Event(0, Rhythm.E), Event(2, Rhythm.E)),
    Lick(Quality.dom, # 1.2
        Event(Note.II, Rhythm.E), Event(3, Rhythm.E),
        Event(0, Rhythm.E), Event(1, Rhythm.E)),
    Lick(Quality.dom, # 1.2
        Event(Note.III, Rhythm.E), Event(-2, Rhythm.E),
        Event(-4, Rhythm.E), Event(-6, Rhythm.E)),
    #Lick(Quality.M, # 1.2
    #    Event(Note.III, Rhythm.Q), Event(Note.REST, Rhythm.Q)),
    Lick(Quality.dom, # 1.3
        Event(Note.VI, Rhythm.E), Event(-1, Rhythm.E),
        Event(-2, Rhythm.E), Event(-3, Rhythm.E)),
    Lick(Quality.dom, # 1.3
        Event(Note.VI, Rhythm.E), Event(-3, Rhythm.E),
        Event(-7, Rhythm.E), Event(-10, Rhythm.E)),
    Lick(Quality.M, # 1.3
        Event(Note.bVII, Rhythm.E), Event(-2, Rhythm.S),
        Event(0, Rhythm.S), Event(-3, Rhythm.E),
        Event(-5, Rhythm.S), Event(-3, Rhythm.S)),
    Lick(Quality.m, # 1.4
        Event(Note.I, Rhythm.E), Event(2, Rhythm.E),
        Event(3, Rhythm.E), Event(5, Rhythm.E)),
    Lick(Quality.m, # 1.4
        Event(Note.V, Rhythm.E), Event(3, Rhythm.E),
        Event(2, Rhythm.E), Event(0, Rhythm.E)),
    Lick(Quality.dom, # 1.4
        Event(Note.I, Rhythm.E), Event(-1, Rhythm.E),
        Event(-2, Rhythm.E), Event(2, Rhythm.E)),
    Lick(Quality.dom, # 1.4
        Event(Note.VI, Rhythm.E), Event(-2, Rhythm.E),
        Event(Note.REST, Rhythm.Q)),
    Lick(Quality.m, # 1.5
        Event(Note.I, Rhythm.E), Event(3, Rhythm.E),
        Event(2, Rhythm.E), Event(0, Rhythm.E)),
    Lick(Quality.m, # 1.5
        Event(Note.IV, Rhythm.E), Event(-3, Rhythm.E),
        Event(-2, Rhythm.T), Event(2, Rhythm.T),
        Event(5, Rhythm.T)),
    Lick(Quality.dom, # 1.5
        Event(Note.VI, Rhythm.E), Event(3, Rhythm.E),
        Event(1, Rhythm.E), Event(0, Rhythm.E)),
    Lick(Quality.dom, # 1.5
        Event(Note.bVI, Rhythm.E), Event(-4, Rhythm.E),
        Event(-8, Rhythm.E), Event(-10, Rhythm.E)),
    Lick(Quality.pu, # 1.6
        Event(Note.REST, Rhythm.Q), Event(0, Rhythm.E),
        Event(2, Rhythm.E)),
    Lick(Quality.m, # 1.6
        Event(Note.bIII, Rhythm.E), Event(2, Rhythm.E),
        Event(-1, Rhythm.E), Event(0, Rhythm.E)),
    Lick(Quality.dom, # 1.6
        Event(Note.III, Rhythm.E), Event(-1, Rhythm.E),
        Event(-2, Rhythm.E), Event(-3, Rhythm.E)),
    Lick(Quality.m, # 1.7
        Event(Note.I, Rhythm.E), Event(2, Rhythm.E),
        Event(5, Rhythm.E), Event(4, Rhythm.E)),
    Lick(Quality.m, # 1.7
        Event(Note.bIII, Rhythm.E), Event(-1, Rhythm.E),
        Event(-3, Rhythm.E), Event(-5, Rhythm.E)),
    Lick(Quality.dom, # 1.7
        Event(Note.III, Rhythm.E), Event(-2, Rhythm.E),
        Event(-4, Rhythm.E), Event(-5, Rhythm.E)),
    Lick(Quality.dom, # 1.7
        Event(Note.bVII, Rhythm.E), Event(4, Rhythm.E),
        Event(-1, Rhythm.E), Event(-3, Rhythm.E)),
    Lick(Quality.m, # 1.8
        Event(Note.I, Rhythm.E), Event(-3, Rhythm.E),
        Event(-7, Rhythm.E), Event(-5, Rhythm.E)),
    Lick(Quality.m, # 1.8
        Event(Note.VI, Rhythm.E), Event(-2, Rhythm.E),
        Event(-4, Rhythm.E), Event(-5, Rhythm.E)),
    Lick(Quality.dom, # 1.8
        Event(Note.bVII, Rhythm.E), Event(4, Rhythm.E),
        Event(7, Rhythm.E), Event(11, Rhythm.E)),
    Lick(Quality.dom, # 1.8
        Event(Note.bVI, Rhythm.E), Event(-4, Rhythm.E),
        Event(-5, Rhythm.E), Event(-7, Rhythm.E)),
    Lick(Quality.m, # 1.9
        Event(Note.I, Rhythm.E), Event(-2, Rhythm.E),
        Event(-3, Rhythm.E), Event(-5, Rhythm.E)),
    Lick(Quality.m, # 1.9
        Event(Note.IV, Rhythm.E), Event(-1, Rhythm.E),
        Event(-2, Rhythm.E), Event(-3, Rhythm.E)),
    Lick(Quality.dom, # 1.9
        Event(Note.V, Rhythm.E), Event(2, Rhythm.E),
        Event(3, Rhythm.E), Event(5, Rhythm.E)),
    Lick(Quality.dom, # 1.9
        Event(Note.bII, Rhythm.E), Event(-1, Rhythm.E),
        Event(7, Rhythm.E), Event(5, Rhythm.E)),
    #Lick(Quality.M, # 1.9
    #    Event(Note.II, Rhythm.Q), Event(Note.REST, Rhythm.Q)),
    #Lick(Quality.M, # 1.9
    #    Event(Note.I, Rhythm.Q), Event(Note.REST, Rhythm.Q)),
    Lick(Quality.m, # 1.10
        Event(Note.V, Rhythm.E), Event(-4, Rhythm.E),
        Event(-5, Rhythm.E), Event(-7, Rhythm.E)),
    Lick(Quality.dom, # 1.10
        Event(Note.I, Rhythm.E), Event(-1, Rhythm.E),
        Event(-2, Rhythm.E), Event(-3, Rhythm.E)),
    Lick(Quality.dom, # 1.11
        Event(Note.VI, Rhythm.E), Event(-2, Rhythm.E),
        Event(-3, Rhythm.E), Event(-5, Rhythm.E)),
    Lick(Quality.m, # 1.12
        Event(Note.I, Rhythm.E), Event(3, Rhythm.E),
        Event(7, Rhythm.E), Event(10, Rhythm.E)),
    Lick(Quality.m, # 1.12
        Event(Note.II, Rhythm.E), Event(-2, Rhythm.E),
        Event(3, Rhythm.E), Event(2, Rhythm.E)),
    Lick(Quality.dom, # 1.12
        Event(Note.bVII, Rhythm.E), Event(-8, Rhythm.E),
        Event(-9, Rhythm.E), Event(-8, Rhythm.E)),
    Lick(Quality.m, # 1.13
        Event(Note.I, Rhythm.E), Event(2, Rhythm.E),
        Event(0, Rhythm.E), Event(-2, Rhythm.E)),
    Lick(Quality.dom, # 1.13
        Event(Note.I, Rhythm.E), Event(-2, Rhythm.E),
        Event(Note.REST, Rhythm.Q)),
    Lick(Quality.m, # 1.14
        Event(Note.V, Rhythm.E), Event(1, Rhythm.E),
        Event(2, Rhythm.E), Event(-2, Rhythm.E)),
    Lick(Quality.dom, # 1.14
        Event(Note.bII, Rhythm.E), Event(1, Rhythm.E),
        Event(-3, Rhythm.E), Event(-2, Rhythm.E)),
    Lick(Quality.m, # 1.15
        Event(Note.I, Rhythm.E), Event(3, Rhythm.E),
        Event(7, Rhythm.Q)),
    Lick(Quality.m, # 1.15
        Event(Note.VII, Rhythm.E), Event(4, Rhythm.E),
        Event(8, Rhythm.Q)),
    Lick(Quality.dom, # 1.15
        Event(Note.IV, Rhythm.E), Event(5, Rhythm.E),
        Event(9, Rhythm.Q)),
    Lick(Quality.m, # 1.16
        Event(Note.I, Rhythm.E), Event(7, Rhythm.E),
        Event(3, Rhythm.E), Event(0, Rhythm.E)),
    Lick(Quality.m, # 1.16
        Event(Note.VII, Rhythm.E), Event(8, Rhythm.E),
        Event(4, Rhythm.E), Event(0, Rhythm.E)),
    Lick(Quality.dom, # 1.16
        Event(Note.IV, Rhythm.E), Event(9, Rhythm.E),
        Event(5, Rhythm.E), Event(0, Rhythm.E)),
    Lick(Quality.m, # 1.17
        Event(Note.I, Rhythm.E), Event(-5, Rhythm.E),
        Event(-9, Rhythm.E), Event(-12, Rhythm.E)),
    Lick(Quality.m, # 1.17
        Event(Note.VII, Rhythm.E), Event(-4, Rhythm.E),
        Event(-8, Rhythm.E), Event(-11, Rhythm.E)),
    Lick(Quality.dom, # 1.17
        Event(Note.IV, Rhythm.E), Event(-3, Rhythm.E),
        Event(-7, Rhythm.E), Event(-10, Rhythm.E)),
    Lick(Quality.m, # 1.18
        Event(Note.I, Rhythm.E), Event(2, Rhythm.E),
        Event(-2, Rhythm.E), Event(0, Rhythm.E)),
    Lick(Quality.dom, # 1.18
        Event(Note.III, Rhythm.E), Event(1, Rhythm.E),
        Event(-2, Rhythm.E), Event(0, Rhythm.E)),
    Lick(Quality.dom, # 1.19
        Event(Note.bIII, Rhythm.Q), Event(-2, Rhythm.T),
        Event(-7, Rhythm.T), Event(-11, Rhythm.T)),
    Lick(Quality.dom, # 1.19
        Event(Note.bIII, Rhythm.E), Event(-2, Rhythm.E + Rhythm.Q)),
    Lick(Quality.dom, # 1.20
        Event(Note.bIII, Rhythm.E), Event(-2, Rhythm.E),
        Event(0, Rhythm.E), Event(-2, Rhythm.E)),
    Lick(Quality.dom, # 1.20
        Event(Note.bIII, Rhythm.E), Event(-2, Rhythm.E),
        Event(-3, Rhythm.E), Event(-5, Rhythm.E)),
    Lick(Quality.m, # 1.21
        Event(Note.II, Rhythm.Q), Event(-2, Rhythm.E),
        Event(0, Rhythm.E)),
    Lick(Quality.dom, # 1.21
        Event(Note.bII, Rhythm.E), Event(3, Rhythm.E),
        Event(7, Rhythm.E), Event(3, Rhythm.E)),
    Lick(Quality.dom, # 1.21
        Event(Note.bV, Rhythm.Q), Event(-2, Rhythm.E),
        Event(-1, Rhythm.E)),
    Lick(Quality.dom, # 1.22
        Event(Note.bVII, Rhythm.Q), Event(0, Rhythm.E),
        Event(2, Rhythm.E)),
    Lick(Quality.dom, # 1.22
        Event(Note.bII, Rhythm.E), Event(-1, Rhythm.E),
        Event(-3, Rhythm.Q)),
    Lick(Quality.dom, # 1.23
        Event(Note.I, Rhythm.E), Event(-3, Rhythm.E),
        Event(-2, Rhythm.E), Event(0, Rhythm.E)),
    Lick(Quality.dom, # 1.23
        Event(Note.bII, Rhythm.E), Event(3, Rhythm.E),
        Event(6, Rhythm.E), Event(12, Rhythm.E)),
    Lick(Quality.m, # 1.24
        Event(Note.I, Rhythm.E), Event(7, Rhythm.E),
        Event(3, Rhythm.T), Event(0, Rhythm.T),
        Event(-5, Rhythm.T)),
    Lick(Quality.m, # 1.24
        Event(Note.VII, Rhythm.E), Event(8, Rhythm.E),
        Event(4, Rhythm.T), Event(0, Rhythm.T),
        Event(-6, Rhythm.T)),
    Lick(Quality.dom, # 1.24
        Event(Note.IV, Rhythm.E), Event(-2, Rhythm.E),
        Event(-1, Rhythm.E), Event(7, Rhythm.E)),
    Lick(Quality.m, # 1.25
        Event(Note.II, Rhythm.E), Event(-2, Rhythm.E),
        Event(-4, Rhythm.E), Event(-7, Rhythm.E)),
    Lick(Quality.dom, # 1.25
        Event(Note.III, Rhythm.E), Event(-9, Rhythm.E),
        Event(-6, Rhythm.E), Event(-1, Rhythm.E)),
    Lick(Quality.dom, # 1.25
        Event(Note.bIII, Rhythm.Q), Event(-2, Rhythm.E),
        Event(-3, Rhythm.E)),

    Lick(Quality.m, # 1.56
        Event(Note.bVII, Rhythm.Q), Event(-3, Rhythm.E),
        Event(-7, Rhythm.E)),

    Lick(Quality.m, # 1.61
        Event(Note.bVII, Rhythm.E), Event(-2, Rhythm.E),
        Event(-1, Rhythm.E), Event(2, Rhythm.E)),

    Lick(Quality.m, # 1.98
        Event(Note.bVII, Rhythm.E), Event(-3, Rhythm.E),
        Event(0, Rhythm.E), Event(4, Rhythm.E)),

    Lick(Quality.m, # 2.15
        Event(Note.bVII, Rhythm.Q), Event(Note.REST, Rhythm.E),
        Event(2, Rhythm.S), Event(5, Rhythm.S)),

    Lick(Quality.M, # 3.1
        Event(Note.V, Rhythm.Q), Event(0, Rhythm.E),
        Event(2, Rhythm.E)),
    Lick(Quality.M, # 3.1
        Event(Note.V, Rhythm.Q), Event(-12, Rhythm.E),
        Event(-10, Rhythm.E)),
    Lick(Quality.M, # 3.1
        Event(Note.VII, Rhythm.Q), Event(0, Rhythm.E),
        Event(1, Rhythm.E)),
    Lick(Quality.M, # 3.1
        Event(Note.VII, Rhythm.E), Event(-2, Rhythm.E),
        Event(-4, Rhythm.Q)),
    Lick(Quality.M, # 3.2
        Event(Note.III, Rhythm.Q + Rhythm.E), Event(-4, Rhythm.E)),
    Lick(Quality.M, # 3.2
        Event(Note.VI, Rhythm.Q), Event(2, Rhythm.Q)),
    Lick(Quality.M, # 3.2
        Event(Note.I, Rhythm.Q), Event(2, Rhythm.Q)),
    Lick(Quality.M, # 3.3
        Event(Note.III, Rhythm.T), Event(1, Rhythm.T),
        Event(2, Rhythm.T), Event(3, Rhythm.T),
        Event(2, Rhythm.T), Event(1, Rhythm.T)),
    Lick(Quality.M, # 3.3
        Event(Note.III, Rhythm.E), Event(-4, Rhythm.E),
        Event(-7, Rhythm.E), Event(-9, Rhythm.E)),
    Lick(Quality.M, # 3.3
        Event(Note.I, Rhythm.Q), Event(0, Rhythm.E),
        Event(-1, Rhythm.E)),
    Lick(Quality.M, # 3.4
        Event(Note.V, Rhythm.T), Event(1, Rhythm.T),
        Event(0, Rhythm.T), Event(-1, Rhythm.E),
        Event(0, Rhythm.E)),
    Lick(Quality.M, # 3.4
        Event(Note.bV, Rhythm.E), Event(1, Rhythm.E),
        Event(2, Rhythm.E), Event(3, Rhythm.E)),
    Lick(Quality.M, # 3.4
        Event(Note.I, Rhythm.E), Event(-5, Rhythm.E),
        Event(-6, Rhythm.E), Event(-7, Rhythm.E)),
    Lick(Quality.M, # 3.4
        Event(Note.III, Rhythm.E), Event(-1, Rhythm.E),
        Event(-2, Rhythm.E), Event(-3, Rhythm.E)),
    Lick(Quality.M, # 3.6
        Event(Note.V, Rhythm.E), Event(2, Rhythm.E),
        Event(4, Rhythm.E), Event(5, Rhythm.E)),
    Lick(Quality.M, # 3.6
        Event(Note.II, Rhythm.E), Event(-3, Rhythm.E),
        Event(-2, Rhythm.E), Event(0, Rhythm.E)),

    Lick(Quality.M, # 3.7
        Event(Note.V, Rhythm.E), Event(-2, Rhythm.E),
        Event(-3, Rhythm.E), Event(-5, Rhythm.E)),
    Lick(Quality.M, # 3.7
        Event(Note.I, Rhythm.E), Event(-1, Rhythm.E),
        Event(2, Rhythm.T), Event(5, Rhythm.T),
        Event(8, Rhythm.T)),
    Lick(Quality.M, # 3.7
        Event(Note.V, Rhythm.E), Event(-2, Rhythm.E),
        Event(-3, Rhythm.Q)),

    Lick(Quality.M, # 3.8
        Event(Note.VII, Rhythm.T), Event(1, Rhythm.T),
        Event(2, Rhythm.T), Event(3, Rhythm.E),
        Event(0, Rhythm.E)),
    Lick(Quality.M, # 3.8
        Event(Note.I, Rhythm.E), Event(-2, Rhythm.E),
        Event(-1, Rhythm.T), Event(2, Rhythm.T),
        Event(5, Rhythm.T)),
    Lick(Quality.M, # 3.8
        Event(Note.bVI, Rhythm.E), Event(-1, Rhythm.Q),
        Event(-6, Rhythm.E)),
    Lick(Quality.M, # 3.9
        Event(Note.VI, Rhythm.E), Event(-1, Rhythm.E),
        Event(-2, Rhythm.E), Event(-4, Rhythm.E)),
    Lick(Quality.M, # 3.9
        Event(Note.III, Rhythm.E), Event(-2, Rhythm.E),
        Event(-4, Rhythm.E), Event(-5, Rhythm.E)),
    Lick(Quality.M, #3.9
        Event(Note.III, Rhythm.E), Event(3, Rhythm.E + Rhythm.Q)),


    Lick(Quality.M, # 3.13
        Event(Note.VII, Rhythm.E), Event(1, Rhythm.E),
        Event(1, Rhythm.E), Event(1, Rhythm.E)),

]
"""Lick(Quality.M,
    Event(Note.VII, Rhythm.Q), Event(Note.REST, Rhythm.Q)),
Lick(Quality.dom,
    Event(Note.I, Rhythm.Q), Event(Note.REST, Rhythm.Q)),
Lick(Quality.dom,
    Event(Note.III, Rhythm.Q), Event(Note.REST, Rhythm.Q)),
Lick(Quality.dom,
    Event(Note.V, Rhythm.Q), Event(Note.REST, Rhythm.Q)),
Lick(Quality.m,
    Event(Note.bVII, Rhythm.Q), Event(Note.REST, Rhythm.Q)),
Lick(Quality.M, # 3.3
Event(Note.REST, Rhythm.E), Event(Note.VII, Rhythm.E),
Event(-4, Rhythm.Q)),"""

"""+ [
Lick(quality,

for quality
in [Quality.M, Quality.dom, Quality.m]
for note
in [Note.I, ]
]
"""
assert len([lick for i, lick in enumerate(licks) if not lick in licks[i+1:]]) == len(licks), "duplicate"
assert all([sum([event.rhythm for event in lick]) == 24 for lick in licks]), "incorrect length"