#ifndef MID_H
#define MID_H

#include "beg.h"

/**
 * Stores the file pointer for a MIDI file as well as the number of bytes
 * in the first (and only) track chunk. Rest is used when a rest is
 * "added" to the MIDI file.
 */
struct midi {
    FILE *fp;
    size_t s;
    int rest;
};

/**
 * Initialize a MIDI file with a name.
 */
void midi_init(struct midi *, char *);

/**
 * Writes a note struct to a MIDI file.
 */
void midi_add(struct midi *, struct note *);

/**
 * Finishes writing and saves a MIDI file.
 */
void midi_close(struct midi *);

#endif