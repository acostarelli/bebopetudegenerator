class Chord:
    def __init__(self, root):
        self.__notes = [root]

    def __add(self, *n):
        self.__notes.extend(note + rel for note, rel in zip(self.__notes, n))

        return self

    def M(self):
        """
        Make the chord major
        """
        return self.__add(4, 7, 11)

    def dom(self):
        """
        Make the chord dominant
        """
        return self.__add(4, 7, 10)

    def m(self):
        """
        Make the chord minor
        """
        return self.__add(3, 7, 10)