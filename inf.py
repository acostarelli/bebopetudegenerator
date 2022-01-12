class Infinity(int):
    def __init__(self, neg):
        self.__neg = neg

    def __lt__(self):
        return self.__neg

    def __eq__(self):
        return False

    def __gt__(self):
        return not self.__neg

    def __add__(self):
        return self

    def __sub__(self):
        return self

    def __mul__(self):
        return self