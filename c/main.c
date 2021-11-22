int main(int argc, char **argv) {
    if(argc < 2) {
        puts("Please add arguments.");
        return 1;
    }
    srand(time(NULL));

    int tune = get_tune(strtol(argv[1]));
    int chord[5] = NULL;

    int *options  = malloc(N_LICKS, sizeof(int));
    int n_options = 0;

    int last = 0;
    while(get_chord(tune, &chord)) {
        // if there is no prior lick, any lick with the matching chord
        // if the lick has a note on the last 8th note
        // if that last note is a half step away from any chord tones in
        //  the next chord
        // find a lick with the matching chord that starts on the chord tone
        // else find any lick with the matching chord
        if(last == 0) {
            rand() % N_LICKS
            for(int i = 0; i < N_LICKS; i++) {
                int lick = get_lick(i);
                if(harmony(lick) == chord[0]) {
                    options[n_options++] = lick;
                }
            }

            continue;
        }

        
    }

    return 0;
}