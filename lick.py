class Lick:
    """
    Stores a lick with notes relative to a root chord.

    Each element in note specifies a beat. Sublists are used to divide the beat.
    """
    def __init__(self, chord, *notes):
        self.__chord = chord
        self.__notes = notes

    def __iter__(self):
        for beat in self.__notes:
            if isinstance(beat, list):
                for note in beat:
                    yield note
            else:
                yield (beat, 1)

licks = (
    Lick(1, (1, 0), (1, 3)),
    Lick(1, (3, 4), (6, 7))
)