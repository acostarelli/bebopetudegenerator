#ifndef TUNES_H
#define TUNES_H

#include "beg.h"

#define TUNE_DELIMITER -1
#define NEW_TUNE , TUNE_DELIMITER,

#define TUNES_LENGTH (size(tunes) / size(int))
const int tunes[] = {
    /* Blues */
    dom(I), dom(IV), dom(I), dom(I)

    /* Rhythm changes */
    NEW_TUNE
    M(I), dom(VI), m(II), dom(V)
};

struct tune {
    struct chord *chords;
};

/**
 * Gets a tune by its index.
 */
void get_tune(int, struct tune *);

/**
 * Gets the next chord in a tune.
 *
 * int   -- the tune ID returned from get_tune
 * **int -- int[] = malloc(4);
 */
void chords_generator(int, struct chord *);

#endif