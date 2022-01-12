from music import Chord, Quality, Note

class Standard:
    def __init__(self, name, *chords):
        self.__name   = name
        self.__chords = chords

    def __iter__(self):
        for chord in self.__chords:
            yield chord

standards = [
    Standard("Oleo",
        Chord(Quality.M, Note.I), Chord(Quality.dom, Note.VI),
        Chord(Quality.m, Note.II), Chord(Quality.dom, Note.V),
        Chord(Quality.m, Note.III), Chord(Quality.dom, Note.VI),
        Chord(Quality.m, Note.II), Chord(Quality.dom, Note.V),
        Chord(Quality.m, Note.V), Chord(Quality.dom, Note.I),
        Chord(Quality.dom, Note.IV), Chord(Quality.dom, Note.bVII),
        Chord(Quality.m, Note.III), Chord(Quality.dom, Note.VI),
        Chord(Quality.m, Note.II), Chord(Quality.dom, Note.V),
        Chord(Quality.M, Note.I), Chord(Quality.dom, Note.VI),
        Chord(Quality.m, Note.II), Chord(Quality.dom, Note.V),
        Chord(Quality.m, Note.III), Chord(Quality.dom, Note.VI),
        Chord(Quality.m, Note.II), Chord(Quality.dom, Note.V),
        Chord(Quality.m, Note.V), Chord(Quality.dom, Note.I),
        Chord(Quality.dom, Note.IV), Chord(Quality.dom, Note.bVII),
        Chord(Quality.m, Note.II), Chord(Quality.dom, Note.V),
        Chord(Quality.M, Note.I), Chord(Quality.M, Note.I),
        Chord(Quality.dom, Note.III), Chord(Quality.dom, Note.III),
        Chord(Quality.m, Note.VII), Chord(Quality.dom, Note.III),
        Chord(Quality.dom, Note.VI), Chord(Quality.dom, Note.VI),
        Chord(Quality.m, Note.III), Chord(Quality.dom, Note.VI),
        Chord(Quality.dom, Note.II), Chord(Quality.dom, Note.II),
        Chord(Quality.m, Note.VI), Chord(Quality.dom, Note.II),
        Chord(Quality.dom, Note.V), Chord(Quality.dom, Note.V),
        Chord(Quality.m, Note.II), Chord(Quality.dom, Note.V),
        Chord(Quality.M, Note.I), Chord(Quality.dom, Note.VI),
        Chord(Quality.m, Note.II), Chord(Quality.dom, Note.V),
        Chord(Quality.m, Note.III), Chord(Quality.dom, Note.VI),
        Chord(Quality.m, Note.II), Chord(Quality.dom, Note.V),
        Chord(Quality.m, Note.V), Chord(Quality.dom, Note.I),
        Chord(Quality.dom, Note.IV), Chord(Quality.dom, Note.bVII),
        Chord(Quality.m, Note.II), Chord(Quality.dom, Note.V),
        Chord(Quality.M, Note.I), Chord(Quality.M, Note.I)),
]