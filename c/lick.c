#include "beg.h"

bool licks_generator(struct lick *l) {
    static i = 0;
    if(i >= NUM_LICKS) {
        i = 0;
    }

    *l = licks[i++];
    return i < NUM_LICKS;
}

bool notes_generator(struct lick l, struct note *n) {
    static _i = 0;
    if(n->notes->dur == 0) {
        i = 0;
    }

    *n = licks + (lick * LICK_LENGTH) + 1 + i;
    i++;

    return n->note != 0;
}