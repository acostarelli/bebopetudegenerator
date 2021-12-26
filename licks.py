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
        return self.__events[0]

    @property
    def last(self):
        return self.__events[-1]

    def __getitem__(self, i):
        return self.__events[i]

    def __iter__(self):
        for event in self.__events:
            yield event

licks = [
    Lick(Quality.m,
        Event(Note.I, Rhythm.E), Event(-1, Rhythm.E),
        Event(0, Rhythm.E), Event(2, Rhythm.E)),
    Lick(Quality.m,
        Event(Note.bIII, Rhythm.E), Event(2, Rhythm.E),
        Event(4, Rhythm.E), Event(7, Rhythm.E)),
    Lick(Quality.dom,
        Event(Note.VI, Rhythm.E), Event(1, Rhythm.E),
        Event(0, Rhythm.E), Event(-2, Rhythm.E)),
    Lick(Quality.dom,
        Event(Note.bV, Rhythm.E), Event(-2, Rhythm.E),
        Event(-3, Rhythm.E), Event(-5, Rhythm.E)),
    Lick(Quality.M,
        Event(Note.V, Rhythm.Q), Event(Note.REST, Rhythm.Q)),
    Lick(Quality.m,
        Event(Note.bIII, Rhythm.E), Event(-1, Rhythm.E),
        Event(0, Rhythm.E), Event(2, Rhythm.E)),
    Lick(Quality.dom,
        Event(Note.II, Rhythm.E), Event(3, Rhythm.E),
        Event(0, Rhythm.E), Event(1, Rhythm.E)),
    Lick(Quality.dom,
        Event(Note.III, Rhythm.E), Event(-2, Rhythm.E),
        Event(-4, Rhythm.E), Event(-6, Rhythm.E)),
    Lick(Quality.M,
        Event(Note.III, Rhythm.Q), Event(Note.REST, Rhythm.Q)),
    Lick(Quality.dom,
        Event(Note.VI, Rhythm.E), Event(-1, Rhythm.E),
        Event(-2, Rhythm.E), Event(-3, Rhythm.E)),
    Lick(Quality.dom,
        Event(Note.VI, Rhythm.E), Event(-3, Rhythm.E),
        Event(-7, Rhythm.E), Event(-10, Rhythm.E)),
    Lick(Quality.M,
        Event(Note.bVII, Rhythm.E), Event(-2, Rhythm.S),
        Event(0, Rhythm.S), Event(-3, Rhythm.E),
        Event(-5, Rhythm.S), Event(-3, Rhythm.S),
        Event(-6, Rhythm.Q)),
    Lick(Quality.m,
        Event(Note.I, Rhythm.E), Event(2, Rhythm.E),
        Event(3, Rhythm.E), Event(5, Rhythm.E)),
    Lick(Quality.m,
        Event(Note.V, Rhythm.E), Event(3, Rhythm.E),
        Event(2, Rhythm.E), Event(0, Rhythm.E)),
    Lick(Quality.dom,
        Event(Note.I, Rhythm.E), Event(-1, Rhythm.E),
        Event(-2, Rhythm.E), Event(2, Rhythm.E)),
    Lick(Quality.dom,
        Event(Note.VI, Rhythm.E), Event(-2, Rhythm.E)),
    Lick(Quality.m,
        Event(Note.I, Rhythm.E), Event(3, Rhythm.E),
        Event(2, Rhythm.E), Event(0, Rhythm.E)),
    Lick(Quality.m,
        Event(Note.IV, Rhythm.E), Event(-3, Rhythm.E),
        Event(-2, Rhythm.T), Event(2, Rhythm.T),
        Event(5, Rhythm.T)),
    Lick(Quality.dom,
        Event(Note.VI, Rhythm.E), Event(3, Rhythm.E),
        Event(1, Rhythm.E), Event(0, Rhythm.E)),
    Lick(Quality.dom,
        Event(Note.bVI, Rhythm.E), Event(-4, Rhythm.E),
        Event(-8, Rhythm.E), Event(-10, Rhythm.E)),
    Lick(Quality.pu,
        Event(Note.REST, Rhythm.Q), Event(0, Rhythm.E),
        Event(2, Rhythm.E)),
    Lick(Quality.m,
        Event(Note.bIII, Rhythm.E), Event(2, Rhythm.E),
        Event(-1, Rhythm.E), Event(0, Rhythm.E)),
    Lick(Quality.dom,
        Event(Note.III, Rhythm.E), Event(-1, Rhythm.E),
        Event(-2, Rhythm.E), Event(-3, Rhythm.E))
]