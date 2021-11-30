#include "beg.h"

size_t lev(char *a, char *b) {
    if(strlen(a) == 0) {
        return strlen(b);
    }
    if(strlen(b) == 0) {
        return strlen(a);
    }
    if(*a == *b) {
        return lev(a + 1, b + 1);
    }

    return fmin(fmin(lev(a + 1, b), lev(a, b + 1)), lev(a + 1, b + 1));
}