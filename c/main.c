#include "beg.h"

int main(int argc, char **argv) {
    struct tune t;
    get_tune(strtol(argv[1], NULL, 10), &t);

    struct etude e;
    etude_init(&e, t);

    struct lick *options = malloc(NUM_LICKS * sizeof(struct lick));
    struct lick *start   = options;

    struct chord c;
    struct lick  l;
    struct note  n;
    while(chords_generator(tune, &c)) {
        while(licks_generator(&l)) {
            if(l.quality == c.quality) {
                *options++ = l;
            }
        }

        // chord generator returns 2 beats
        // all licks are 2 beats

        l = options[rand() % (options - start)];
        while(notes_generator(l, &n)) {
            n.note += root + c.root;
            etude_add(&n);
        }

        options = start;
    }

    struct mid m;
    midi_init(&m, "etude.mid");
    etude_export_mid(&m);
}