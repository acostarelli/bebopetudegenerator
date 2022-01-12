from itertools import islice
from random import choice, sample

def syllgen():
    i = False
    g = sample([
        "aeiou",
        "bcdfghjklmnpqrstvwxyz"
    ], 2)

    while True:
        yield choice(g[i])
        i = not i

def word(n):
    return "".join(islice(syllgen(), n))

if __name__ == "__main__":
    print(word(6))