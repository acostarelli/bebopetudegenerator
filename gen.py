from random import choice

from etude import Etude

def generate(standard, licks):
    e = Etude(standard)

    for chord in standard:
        try:
            e.add(choice([lick for lick in licks if lick.chord.quality == chord.quality]))
        except:
            print("no lick for chord", chord)

    return e