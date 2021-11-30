#include "beg.h"

int main(int argc, char **argv) {
    struct tune t;
    get_tune(strtol(argv[1], NULL, 10), &t);

    struct etude e;
    etude_init(&e, t);

    struct lick *options = malloc(NUM_LICKS * sizeof(struct lick));
    struct lick *start   = options;

    struct chord c;
    struct lick  l;
    struct note  n;
    while(chords_generator(tune, &c)) {
        while(licks_generator(&l)) {
            if(l.quality == c.quality) {
                *options++ = l;
            }
        }

        // chord generator returns 2 beats
        // all licks are 2 beats

        l = options[rand() % (options - start)];
        while(notes_generator(l, &n)) {
            n.note += root + c.root;
            etude_add(&n);
        }

        options = start;
    }

    struct mid m;
    midi_init(&m, "etude.mid");
    etude_export_mid(&m);
}

enum quality {
    MAJOR,
    DOMINANT,
    MINOR
};

struct chord {
    enum quality quality;
    int root;
    int third;
    int fifth;
    int seventh;
};

/**
 * Compile-time chord structures.
 */
#define M(r)   { MAJOR,    r, 4 + r, 7 + r, 11 + r }
#define dom(r) { DOMINANT, r, 4 + r, 7 + r, 10 + r }
#define m(r)   { MINOR,    r, 3 + r, 7 + r, 10 + r }

/**
 * Semitones above root.
 */
#define I   0
#define II  2
#define III 4
#define IV  5
#define V   7
#define VI  9
#define VII 11
#define SIV 6

#define TUNE_END { 0, 0, 0, 0, 0 };
#define TUNE_IS_END(c) (c.quality == 0 && c.root == 0 && c.third == 0 && c.fifth == 0 && c.seventh == 0)

struct chord tunes[][17] = {
    /* Blues */
    { dom(I), dom(IV), dom(I), dom(I), dom(IV), dom(IV), dom(I), dom(I), TUNE_END }
};

struct note {
    int dur;
    int note;
};

#define RQ 12,
#define RE 6,
#define RT 4,
#define RS 3,
#define REST INT_MIN

#define LICK_END { 0, 0 };
#define LICK_IS_END(n) (n.dur == 0 && n.note == 0)

struct note licks[][17] = {
    { RQ 0, LICK_END }
};

int main(int argc, char **argv) {
    int tune_i = tunes[strtol(argv[1], NULL, 10)];

    for(struct chord *c; !TUNE_IS_END(*c); c++) {
        for(struct note *n; !LICK_IS_END(*n); n++) {
            
        }
    }
}