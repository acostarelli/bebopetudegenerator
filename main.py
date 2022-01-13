from random import choice, choices
from itertools import combinations

from mido import MidiFile, MidiTrack, Message

from music import Rhythm, Event, Note
from standards import standards
from licks import licks

from pprint import pprint
import sys

iterbreak_n = -1
def iterbreak(n):
    global iterbreak_n
    if iterbreak_n == 1:
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

def chrommy(lick):
    return sum(abs(a-b) for a, b in combinations([0] + [event.note for note in lick[1:]], 2)) / len(lick)

### 61 to 92
def weighter(lick, last, chord):
    weight = 0

    if lick.quality != chord.quality:
        return 0

    diff = abs((last % 12) - (chord.root + lick.first.note) % 12)
    #[abs(((tone + chord.root) % 12) - (last % 12)) for tone in chord.quality]
    diff = diff - (12 * (diff // 6))
    if diff == 1: # this is flawed... licks that aren't 1 away will get away with this
    # you want to say: if the last note is a half step away from a chord tone, choose licks that start on that chord tone
        if lick.first.note in chord.quality:
            return 1
        else:
            return 0
        #return 1
    elif diff in [2, 3]:
        return 1

    return 0

def v1random(standard):
    last = 72
    events = []
    for chord in standard:
        print("chord:", chord.root)
        print("last:", last)
        # could make this into a generator, and use next() to get the lick that stays within range
        # one part selects the lick, the next part turns it into real notes
        while True:
            #i, lick = choices(list(enumerate(licks)), weights=[weighter(lick, last, chord) for lick in licks])[0]
            i, lick = choices(list(enumerate(licks)))[0]
            print("lick:", i+1)
            #first = (((chord.root + lick[0].note) % 12) - 6) + (12 * round(last / 12))
            first = (chord.root + lick.first.note) % 12
            print("cock", first, chord.root, lick.first.note)
            first = [0, 1, 2, 3, 4, 5, 6, -5, -4, -3, -2, -1][first]

            print("m ", first)
            print("n ", last)
            print((-1/12) * (first - last - 6), (-1/12) * (first - last + 6))
            print(int((-1/12) * (first - last - 6)))

            first = first + 12*(int((-1/12) * (first - last - 6)))
            #first = first + (12 * round(last / 12))

            events = [Event(first, lick[0].rhythm)] + [Event(first + event.note, event.rhythm) for event in lick[1:]]
            print([event.note for event in lick])
            print([event.note for event in events])
            print("#")

            #iterbreak(3)

            if all((event.note >= 61 and event.note <= 92) or event.note == Note.REST for event in events):
                break

        print("-------------")

        yield from events
        last = next(event for event in reversed(events) if event.note != Note.REST).note

"""

-5 <= n <= 6    (first note)
0 <= m <= 127   (last note)
0 < c <= 10     (octave multiplier)

j = n + 12c     (realized first note)
|m - j| <= 6    (under a tritone away)

-6 <= m - n - 12c <= 6

------------

|m - n - 12c| <= 6

m - n - 12c <= 6
-m + n + 12c >= -6
12c >= n - m - 6
c >= (n - m - 6) / 12

m - n - 12c <= -6


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