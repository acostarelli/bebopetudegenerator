from collections import namedtuple
from enum import Enum, IntEnum
from sys import argv
from random import choice

from mido import MidiFile, MidiTrack, Message

Rhythm  = IntEnum("Rhythm", "QUARTER EIGHTH TRIPLET SIXTEENTH")
Quality = Enum("Quality", "MAJOR DOMINANT MINOR")
Tone    = IntEnum("Tone", "I bII II bIII III IV bV V bVI VI bVII VII")

Note  = namedtuple("Note",  "rhythm tone")
Lick  = namedtuple("Lick",  "quality notes")
Chord = namedtuple("Chord", "quality root third fifth seventh")
Tune  = namedtuple("Tune",  "name root chords")

# replace with parsing functions later
def M(r):
    return Chord(Quality.MAJOR,    r, r + Tone.III,  r + Tone.V, r + Tone.VII)

def dom(r):
    return Chord(Quality.DOMINANT, r, r + Tone.III,  r + Tone.V, r + Tone.bVII)

def m(r):
    return Chord(Quality.MINOR,    r, r + Tone.bIII, r + Tone.V, r + Tone.bVII)

tunes = [
    Tune("Blues", 60, [dom(Tone.I), dom(Tone.IV), dom(Tone.I), dom(Tone.I)])
]

def Q(t):
    return Note(Rhythm.QUARTER, t)

def E(t):
    return Note(Rhythm.EIGHTH, t)

def T(t):
    return Note(Rhythm.TRIPLET, t)

def S(t):
    return Note(Rhythm.SIXTEENTH, t)

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
        etude.add(choice([lick for lick in licks if lick.quality == chord.quality]))

    etude.mid()