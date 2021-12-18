#ifndef LIB_H
#define LIB_H

#define LEN(l) size(l) / size(l[0])

/**
 * Calculates the Levenshtein distance between two strings.
 */
size_t lev(char *, char *);

#endif