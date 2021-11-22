#include "beg.h"

void midi_init(struct midi *m, char *name) {
    m->fp = fopen(name, "w");
    m->s  = 0;

    const char header[] = {
        'M', 'T', 'h', 'd', 0, 0, 0, 6, 0, 0, 0, 1, 0, 12, 'M', 'T', 'r', 'k'
    };
    fwrite(header, 1, 18, m->fp);
}

void midi_add(struct midi *m, struct note *n) {

}

void midi_close(struct midi *m) {
    // write track size n shit

    fclose(m->fp);
    free(m);
}