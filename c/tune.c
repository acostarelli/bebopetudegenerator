#include "beg.h"

int get_tune(int i) {
    int ret = 0;
    int n   = 0;

    for(int j = 0; j < TUNES_LENGTH-1; j++) {
        if(n == i) {
            return ret;
        }

        if(tunes[j] == -1) {
            ret = tunes[j+1];
            n++;
        }
    }

    return 0;
}

bool get_chord(int tune, int **chord) {
    if(*chord == NULL) {
        *chord = tunes[tune];
        return true;
    }

    *chord += 4;
    return **chord != -1;
}