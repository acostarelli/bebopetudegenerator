class Event:
    def __init__(self, note, rhythm):
        self.__note   = note
        self.__rhythm = rhythm

class Note:
    I   = 0
    II  = 2
    III = 4
    IV  = 5
    V   = 7
    VI  = 9
    VII = 11
    REST = 12

class Rhythm:
    Q = 12
    E = 6
    T = 4
    S = 3

# can make this a fancy enum
class Quality:
    M   = auto()
    dom = auto()
    m   = auto()

class Lick:
    def __init__(self, quality, *events):
        self.__quality = quality
        self.__events  = events

    @property
    def quality(self):
        return self.__quality

    def __iter__(self):
        return self.__events

class Chord:
    def __init__(self, quality, root):
        self.__quality = quality
        self.__root    = root

    @property
    def quality(self):
        return self.__quality

class Standard:
    def __init__(self, *chords):
        self.__chords = chords

    def __iter__(self):
        return self.__chords

licks = [
    Lick(Quality.M, Event())
]

standards = [
    Standard(Chord(Quality.M, Note.I))
]

def v1random(standard):
    for chord in standard:
        lick = choice([lick for lick in licks if lick.quality == chord.quality])

        for event in lick:
            yield event

if __name__ == "__main__":
    mid = MidiFile(ticks_per_beat=Note.Q)
    trk = MidiTrack()
    mid.tracks.append(trk)

    root = 0
    delay = 0
    for event in v1random(blues):
        if event.note == Note.REST:
            delay += event.rhythm
            continue

        trk.append(Message("note_on",  note=0, ticks=0))
        trk.append(Message("note_off", note=0, ticks=event.rhythm+delay))

        delay = 0