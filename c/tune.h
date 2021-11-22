#ifndef TUNES_H
#define TUNES_H

#include "beg.h"

#define NEW_TUNE , -1,
#define TUNES_LENGTH size(tunes) / size(int);

/**
 * Compile-time structure.
 */
const int tunes[] = {
    /* Blues */
    dom(I), dom(IV), dom(I), dom(I)

    /* Rhythm changes */
    NEW_TUNE
    M(I), dom(VI), m(II), dom(V)
};

/**
 * Gets a tune by its index.
 */
int get_tune(int);

/**
 * Gets the next chord in a tune.
 *
 * int   -- the tune ID returned from get_tune
 * **int -- int[] = malloc(4);
 */
void get_chord(int, **int);

#endif