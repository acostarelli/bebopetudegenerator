#ifndef ETUDE_H
#define ETUDE_H

#include "beg.h"

struct etude {
    struct tune tune;
    struct note *notes;
};

/**
 * Initialize an etude structure; allocate memory for notes.
 */
void etude_init(struct etude *, struct tune);

/**
 * Add a note to the etude and adjust its note value based on the key and
 * current chord.
 */
void etude_add(struct etude *, struct note *);

/**
 * Exports an etude to MIDI.
 */
void etude_export_mid(struct etude *, struct mid *);

#endif