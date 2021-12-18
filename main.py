from random import choice

from mido import MidiFile, MidiTrack, Message

from music import Rhythm, Event, Note
from standards import standards
from licks import licks

def v1random(standard):
    key = 60
    last = None
    for chord in standard:
        lick = choice([lick for lick in licks if lick.quality == chord.quality])

        correction = 0
        if last and last != Note.REST and lick.first.note != Note.REST:
            correction = -12 * int(((key + chord.root + lick.first.note) - last) / 12)

        for event in lick:
            last = key + chord.root + event.note + correction
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