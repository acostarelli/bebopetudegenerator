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

#define NEW_LICK , INT_MAX,

#define LICKS_NUMBER size(licks) / size(int)

const int licks[] = {
    MINOR, RE 0, RE -1, RE 0, RE 2 NEW_LICK
    MINOR, RE 3, RE 5, RE 7, RE 10 NEW_LICK
};
#define N_LICKS 2 /* Manually maintined for runtime performance's sake. */

struct note {
    int note;
    int dur;
};

/**
 * Analogous to get_chord. Returns an identifier for a lick by index.
 */
int get_lick(int);

#endif