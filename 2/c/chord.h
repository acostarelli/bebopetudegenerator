#ifndef CHORD_H
#define CHORD_H

/**
 * All chords are defined with preprocessor macros so that tunes and licks
 * are created at compile-time.
 */

/**
 * Number of semitones above root.
 */
#define I   0
#define II  2
#define III 4
#define IV  5
#define V   7
#define VI  9
#define VII 11
#define SIV 6

#define CHORD_QUALITY(chord) (chord[0])
#define CHORD_ROOT(chord)    (chord[1])

enum quality { MAJOR, DOMINANT, MINOR };

struct chord {
    enum quality quality;
    int root;
    int third;
    int fifth;
    int seventh;
};

/**
 * Given a chord root relative to some key, gives the root, third, fifth
 * and seventh.
 *
 * TODO: Give a chord-scale, and each different chord-scales can go to
 * different types of chord.
 */
#define M(r)   MAJOR,    0 + r, 4 + r, 7 + r, 11 + r
#define dom(r) DOMINANT, 0 + r, 4 + r, 7 + r, 10 + r
#define m(r)   MINOR,    0 + r, 3 + r, 7 + r, 10 + r

#endif