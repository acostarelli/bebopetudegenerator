from argparse import ArgumentParser

from lick     import licks
from standard import standards

def lev(a, b):
    """
    Levenshtein distance.
    """

    if len(b) == 0:
        return len(a)

    if len(a) == 0:
        return len(b)

    if a[0] == b[0]:
        return lev(a[1:], b[1:])

    return 1 + min(
        lev(a[1:], b),
        lev(a, b[1:]),
        lev(a[1:], b[1:])
    )

if __name__ == "__main__":
    parser = ArgumentParser("Command-line bebop etude generator")
    parser.add_argument("standard", nargs=1, help="name of the standard")
    parser.add_argument("-f", "--format", nargs=1, choices=("mid", "abc"), required=True, help="output format")
    args = parser.parse_args()

    generate(
        min(standards, key=lambda s: lev(s.name, args.standard)),
        licks
    ).save(args.format)