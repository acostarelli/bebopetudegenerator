#include "beg.h"

void etude_init(struct etude *e, struct tune t) {
    e->tune  = t;
    e->notes = malloc(10);
}

void etude_add(struct etude *e, struct note *n) {
    // can increment tune pointer to add notes... using chord generator, actually
}