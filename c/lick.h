#ifndef LICK_H
#define LICK_H

#include "beg.h"

/**
 * Beats are divided into 12 parts. "R" = rhythm.
 */
#define RQ 12,
#define RE 6,
#define RT 4,
#define RS 3,
#define REST INT_MIN

#define END_LICK ,0, 0
#define LICK_LENGTH 18

/**
 * All licks are grouped into one vector because I may iterate through all the
 * licks and have odds of selecting from at least two different qualities in
 * the case that I might do a fancy substituion (e.g. VI7 on a turnaround).
 */
const int licks[][LICK_LENGTH] = {
    { MINOR, RE 0, RE -1, RE 0, RE 2  END_LICK},
    { MINOR, RE 3, RE 5 , RE 7, RE 10 END_LICK},
};
#define NUM_LICKS 2 /* Manually maintained for runtime comp. efficiency. */
// todo: can I calculate this easy?

struct note {
    int dur;
    int note;
};

struct lick {
    int id;
    struct note *n;
};

/**
 * Get lick
 */
void get_lick(int id);

/**
 * Returns the next lick each subsequent call.
 */
bool licks_generator(int *);

/**
 * Returns the next note in a lick each subsequent call.
 */
bool notes_generator(int, struct note *);

#endif