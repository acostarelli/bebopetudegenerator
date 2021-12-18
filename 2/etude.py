from mido import Message, MidiFile, MidiTrack

class Etude:
    def __init__(self, standard, key=60):
        self.__standard = iter(standard)
        self.__key      = key
        self.__notes    = []

    def add(self, lick):
        root = next(self.__standard).root
        self.__notes.extend(self.__key + root + note for note in lick)

    def transpose(self, d):
        self.__notes = (note + d for note in self.__notes)
        self.__key   = self.__key + d

    def save(self, format):
        if format == "mid":
            return self.mid()

        if format == "abc":
            return self.abc()

        return None

    def mid(self):
        print(self.__notes)

        mid = MidiFile()
        trk = MidiTrack()
        mid.tracks.append(trk)

        t = int(mid.ticks_per_beat / 2);

        for note in self.__notes:
            trk.append(Message("note_on",  note=note, time=0))
            trk.append(Message("note_off", note=note, time=t))

        mid.save("etude.mid")

    def abc(self):
        pass