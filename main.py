from random import choice, choices

from mido import MidiFile, MidiTrack, Message

from music import Rhythm, Event, Note
from standards import standards
from licks import licks

from pprint import pprint

def v1random(standard):
    """
    Chooses licks based on the previous note and the first note of the lick.
    """
    weights = [
        0, # unison
        4, # m2
        2, # M2
        2, # m3
        2, # M3
        0, # P4
        0, # d5
        0, # P5
        0, # m6
        0, # M6
        0, # m7
        0  # M7
    ]
    cvt = [0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]

    key = 60
    last = None
    for chord in standard:
        if last and last != Note.REST:
            lick = choices(
                [lick for lick in licks if lick.quality == chord.quality],
                weights=[weights[cvt[abs((last % 12) - (chord.root + lick.first.note) % 12)]] for lick in licks if lick.quality == chord.quality]
            )[0]
        else:
            lick = choice([lick for lick in licks if lick.quality == chord.quality])
        first = key + chord.root + lick.first.note

        correction = 0
        if last and last != Note.REST and lick.first.note != Note.REST:
            correction = 6 * int((last - first) / 6)

        first += correction
        yield Event(first, lick.first.rhythm)

        for event in lick[1:]:
            last = first + event.note
            yield Event(last, event.rhythm)

"""
1. no weird octaves
2. smarter lick selection
"""

if __name__ == "__main__":
    mid = MidiFile(ticks_per_beat=Rhythm.Q)
    trk = MidiTrack()
    mid.tracks.append(trk)

    delay = 0
    for event in v1random(standards[0]):
        if event.note == Note.REST:
            delay += event.rhythm
            continue

        trk.append(Message("note_on",  note=event.note, time=delay))
        trk.append(Message("note_off", note=event.note, time=event.rhythm))

        delay = 0

    mid.save("etude.mid")