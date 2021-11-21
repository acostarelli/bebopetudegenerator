from chord import Chord

class Standard:
    def __init__(self, name, *chords):
        self.__name   = name
        self.__chords = chords

    @property
    def name(self):
        return self.__name

    def __iter__(self):
        """
        Returns 
        """
        for measure in self.__chords:
            if isinstance(measure, list):
                for chord in measure:
                    yield (chord, 2)
            else:
                yield (measure, 4)

standards = (
    Standard("Blues",
        Chord(0).dom(), Chord(5).dom(), Chord(0).dom(), Chord(0).dom(),
        Chord(5).dom(), Chord(5).dom(), Chord(0).dom(), Chord(0).dom(),
        Chord(7).dom(), Chord(5).dom(), Chord(0).dom(), Chord(7).dom()),
    Standard("Foo")
)