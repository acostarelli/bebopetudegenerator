from collections import namedtuple
from enum import Enum, IntEnum
from sys import argv
from random import choice

from mido import MidiFile, MidiTrack, Message

Rhythm  = IntEnum("Rhythm", "QUARTER EIGHTH TRIPLET SIXTEENTH")
Quality = Enum("Quality", "MAJOR DOMINANT MINOR")
Tone    = IntEnum("Tone", "I bII II bIII III IV bV V bVI VI bVII VII REST")

Note  = namedtuple("Note",  "rhythm tone")
Lick  = namedtuple("Lick",  "quality notes")
Tune  = namedtuple("Tune",  "name root chords")

class Chord:
    def __init__(self, *tones):
        self.__tones = tones

    def __call__(self, root):
        return (root + tone for tone in tones)

    def __eq__(self, t):
        return self.__tones == t.__tones

M   = Chord(Tones.I, Tones.III,  Tones.V, Tones.VII)
dom = Chord(Tones.I, Tones.III,  Tones.V, Tones.bVII)
m   = Chord(Tones.I, Tones.bIII, Tones.V, Tones.bVII)

tunes = [
    Tune("Blues", 60, [
        dom(Tones.I), dom(Tones.IV), dom(Tones.I), dom(Tones.I)
    ])
]

licks = [
    Lick(Quality.MINOR, [
        Note(Rhythm.EIGHTH, Tone.I),
        Note(Rhythm.EIGHTH, Tone.II),
        Note(Rhythm.EIGHTH, Tone.III),
        Note(Rhythm.EIGHTH, Tone.IV)
    ]),
    Lick(Quality.DOMINANT, [
        Note(Rhythm.EIGHTH, Tone.I),
        Note(Rhythm.EIGHTH, Tone.II),
        Note(Rhythm.EIGHTH, Tone.III),
        Note(Rhythm.EIGHTH, Tone.IV)
    ]),
    Lick(Quality.MAJOR, [
        Note(Rhythm.EIGHTH, Tone.I),
        Note(Rhythm.EIGHTH, Tone.II),
        Note(Rhythm.EIGHTH, Tone.III),
        Note(Rhythm.EIGHTH, Tone.IV)
    ]),
]

class Etude:
    def __init__(self, tune):
        self.__tune  = tune
        self.__notes = []

    @property
    def last(self):
        return self.__notes[-1]

    def add(self, lick):
        self.__notes.extend([Note(note.rhythm, note.tone + self.__tune.root) for note in lick.notes])

    def mid(self):
        mid = MidiFile()
        trk = MidiTrack()
        mid.tracks.append(trk)

        for note in self.__notes:
            trk.append(Message("note_on",  note=note.tone, time=0))
            trk.append(Message("note_off", note=note.tone, time=int(mid.ticks_per_beat / note.rhythm)))

        mid.save("etude.mid")

def lev(a, b):
    if len(a) == 0:
        return len(b)

    if len(b) == 0:
        return len(a)

    if a[0] == b[0]:
        return lev(a[1:], b[1:])

    return 1 + min(
        lev(a[1:], b),
        lev(a, b[1:]),
        lev(a[1:], b[1:])
    )

if __name__ == "__main__":
    tune  = min(tunes, key=lambda t: lev(t.name, argv[1]))
    etude = Etude(tune)

    for chord in tune.chords:
        for i in range(2):
            """
            If the last note in the etude is not a rest
            If the the last note is a half step from
            """
            if etude.last.tone != Tone.REST:
                etude.add(choice([lick for lick in licks if lick.chord == chord and abs(lick.notes[-1].tone - etude.last.note) == 1]))
            else:
                etude.add(choice([lick for lick in licks if lick.chord == chord]))

    etude.mid()