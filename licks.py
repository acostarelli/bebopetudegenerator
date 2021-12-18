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

    def __iter__(self):
        for event in self.__events:
            yield event

licks = [
    Lick(Quality.m,
        Event(Note.I, Rhythm.E), Event(Note.VII, Rhythm.E),
        Event(Note.I, Rhythm.E), Event(Note.II, Rhythm.E)),
    Lick(Quality.m,
        Event(Note.bIII, Rhythm.E), Event(Note.VI, Rhythm.E),
        Event(Note.V, Rhythm.E), Event(Note.bVII, Rhythm.E)),
    Lick(Quality.dom,
        Event(Note.VI, Rhythm.E), Event(Note.bVII, Rhythm.E),
        Event(Note.VI, Rhythm.E), Event(Note.V, Rhythm.E)),
    Lick(Quality.dom,
        Event(Note.bV, Rhythm.E), Event(Note.III, Rhythm.E),
        Event(Note.bIII, Rhythm.E), Event(Note.bII, Rhythm.E)),
    Lick(Quality.M,
        Event(Note.V, Rhythm.Q), Event(Note.REST, Rhythm.Q)),
    Lick(Quality.m,
        Event(Note.bIII, Rhythm.E), Event(Note.II, Rhythm.E),
        Event(Note.bIII, Rhythm.E), Event(Note.IV, Rhythm.E)),
    Lick(Quality.dom,
        Event(Note.II, Rhythm.E), Event(Note.IV, Rhythm.E),
        Event(Note.II, Rhythm.E), Event(Note.bIII, Rhythm.E)),
    Lick(Quality.dom,
        Event(Note.III, Rhythm.E), Event(Note.II, Rhythm.E),
        Event(Note.I, Rhythm.E), Event(Note.bVII, Rhythm.E)),
    Lick(Quality.M,
        Event(Note.III, Rhythm.Q), Event(Note.REST, Rhythm.Q)),
    Lick(Quality.dom,
        Event(Note.VI, Rhythm.E), Event(Note.bVI, Rhythm.E),
        Event(Note.V, Rhythm.E), Event(Note.bV, Rhythm.E)),
    Lick(Quality.dom,
        Event(Note.VI, Rhythm.E), Event(Note.II, Rhythm.E),
        Event(Note.bVII, Rhythm.E), Event(Note.V, Rhythm.E)),
    Lick(Quality.M,
        Event(Note.bVII, Rhythm.E), Event(Note.bVI, Rhythm.S),
        Event(Note.bVII, Rhythm.S), Event(Note.V, Rhythm.E),
        Event(Note.IV, Rhythm.S), Event(Note.V, Rhythm.S),
        Event(Note.III, Rhythm.Q)),
    Lick(Quality.m,
        Event(Note.I, Rhythm.E), Event(Note.II, Rhythm.E),
        Event(Note.bIII, Rhythm.E), Event(Note.IV, Rhythm.E)),
    Lick(Quality.m,
        Event(Note.V, Rhythm.E), Event(Note.bVII, Rhythm.E),
        Event(Note.VI, Rhythm.E), Event(Note.V, Rhythm.E)),
    Lick(Quality.dom,
        Event(Note.I, Rhythm.E), Event(Note.VII, Rhythm.E),
        Event(Note.bVII, Rhythm.E), Event(Note.II, Rhythm.E)),
    Lick(Quality.dom,
        Event(Note.VI, Rhythm.E), Event(Note.V, Rhythm.E)),
    Lick(Quality.m,
        Event(Note.I, Rhythm.E), Event(Note.bIII, Rhythm.E),
        Event(Note.II, Rhythm.E), Event(Note.I, Rhythm.E)),
    Lick(Quality.m,
        Event(Note.IV, Rhythm.E), Event(Note.II, Rhythm.E),
        Event(Note.bIII, Rhythm.T), Event(Note.V, Rhythm.T),
        Event(Note.bVII, Rhythm.T)),
    Lick(Quality.dom,
        Event(Note.VI, Rhythm.E), Event(Note.I, Rhythm.E),
        Event(Note.bVII, Rhythm.E), Event(Note.VI, Rhythm.E)),
    Lick(Quality.dom,
        Event(Note.bVI, Rhythm.E), Event(Note.III, Rhythm.E),
        Event(Note.I, Rhythm.E), Event(Note.bVII, Rhythm.E)),
    Lick(Quality.pu,
        Event(Note.I, Rhythm.E), Event(Note.II, Rhythm.E)),
    Lick(Quality.m,
        Event(Note.bIII, Rhythm.E), Event(Note.IV, Rhythm.E),
        Event(Note.II, Rhythm.E), Event(Note.bIII, Rhythm.E)),
    Lick(Quality.dom,
        Event(Note.III, Rhythm.E), Event(Note.bIII, Rhythm.E),
        Event(Note.II, Rhythm.E), Event(Note.bII, Rhythm.E))
]