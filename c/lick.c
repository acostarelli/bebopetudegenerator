#include "beg.h"

bool licks_generator(int *lick) {
    static i = 0;
    if(*lick == NULL) {
        i = 0;
    }

    *lick = licks[i++];
    return i < NUM_LICKS;
}

bool notes_generator(struct lick l, struct note *n) {
    static i = 0;
    if(*n == NULL) {
        i = 0;
    }

    *n = licks + (lick * LICK_LENGTH) + 1 + i;
    i++;

    return n->note != 0;
}