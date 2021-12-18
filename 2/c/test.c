#include <stdio.h>

int main(int argc, char **argv) {
    for(int j = 0; j < 10; j++) {
        int i = test();
        printf("%d\n", i);
    }

    return 0;
}

int test() {
    static int i = 0;
    i++;
    return i;
}