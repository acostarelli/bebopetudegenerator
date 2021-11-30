#include "beg.h"

int get_tune(int id, struct tune *t) {
    int n = 0;

    for(int i = 0; i < TUNES_LENGTH-1; i++) {
        if(n == i) {
            t->c = i;
            return 1;
        }

        if(tunes[i] == TUNE_DELIMITER) {
            n++;
        }
    }

    return 0;
}

bool chords_generator(struct tune t, struct chord *c) {
    static int i = 0;
    if(*c == 0) {
        i = 0;
    }

    *c = tune.chords[i++];
    return *c != TUNE_DELIMITER;
}