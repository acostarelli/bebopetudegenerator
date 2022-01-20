from random import choice, choices, randrange
from itertools import combinations

from mido import MidiFile, MidiTrack, Message, MetaMessage, bpm2tempo

from music import Rhythm, Event, Note
from standards import standards
from licks import licks

from pprint import pprint
import sys

iterbreak_n = -1
def iterbreak(n):
    global iterbreak_n
    if iterbreak_n == 1:
        print("ITERBROKEN")
        sys.exit(1)

    if iterbreak_n != -1:
        iterbreak_n -= 1

    if iterbreak_n == -1:
        iterbreak_n = n - 1

"""
- give chromatic score; maybe choose lower chromatic licks for first 2 beats
and higher for the transition? or only for dommy licks?
- keep within a given range (db2 - bb5)
- possible substitutions
- as you go higher, weigh licks that go down, vice versa
- give slight weight to licks that maintain direction
- if you split up weight functions, have each return a 1 or a 0, and then
the caller can determine the weight
- probably easier to determine octaves if you start on 0
- maybe if there is a half stepper, just block all others...
"""

def closest_octave(n, t):
    """
    n -- the pitch to correct
    t -- the target pitch

    Returns a new n pitch such that it is no more than a tritone away from t.

    r = n + 12c   (r is the same note as n but as close to m as possible)
    |t - r| <= 6  (solve for c, return r)
    """
    return n + 12 * int((1/12) * (-n + t + 6))

def diff(n, t):
    """
    Returns the difference between n and t <= a tritone.
    """
    return abs(t - closest_octave(n, t))

def weighter(lick, last, chord):
    """
    - Throw out any licks that don't match chord quality
    - If the last note is a half-step from a chord tone
        - Keep this lick if it starts on that chord tone
        - Toss if it doesn't
    - Keep this lick if it's 1, 2, or 3 half-steps away from the last note
    """
    if lick.quality != chord.quality:
        return 0

    try:
        tone = chord.quality[
            next(i
                for i, diff
                in enumerate(
                    diff(tone + chord.root, last)
                    for tone
                    in chord.quality)
                if diff == 1)
        ]

        if not (61 <= closest_octave(tone + chord.root, last) <= 92):
            raise StopIteration

        return lick.first.note == tone

    except StopIteration:
        return diff(lick.first.note + chord.root, last) in range(1, 5) # maybe allow greater for like major chords

def v1random(standard):
    last = randrange(72, 84)
    events = []
    for i, chord in enumerate(standard):
        while True:
            lick = choices(licks, weights=[weighter(lick, last, chord) for lick in licks])[0]
            first = closest_octave(chord.root + lick.first.note, last)

            # this will totally break if the first event is a rest
            events = [Event(first, lick[0].rhythm)] + [Event(first + event.note, event.rhythm) for event in lick[1:]]

            if all((event.note >= 61 and event.note <= 92) or event.note == Note.REST for event in events):
                break

        yield from events
        last = next(event for event in reversed(events) if event.note != Note.REST).note

if __name__ == "__main__":
    mid = MidiFile(ticks_per_beat=Rhythm.Q)
    trk = MidiTrack()
    mid.tracks.append(trk)

    trk.append(MetaMessage("set_tempo", tempo=bpm2tempo(240)))

    delay = 0
    for event in v1random(standards[2]):
        if event.note == Note.REST:
            delay += event.rhythm
            continue

        trk.append(Message("note_on",  note=event.note, time=delay))
        trk.append(Message("note_off", note=event.note, time=event.rhythm))

        delay = 0

    bkg = MidiTrack()
    mid.tracks.append(bkg)
    for chord in standards[2]:
        bkg.append(Message("note_on",  note=chord.root+36, time=0))
        bkg.append(Message("note_off", note=chord.root+36, time=Rhythm.Q+Rhythm.Q))

    mid.save("etude.mid")