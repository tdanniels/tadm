#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MATCH 0
#define INSERT 1
#define DELETE 2
#define SWAP 3

#define NO_PARENT 4

#define MAXLEN 100

typedef struct
{
    size_t cost;
    size_t parent;
} cell;

void row_init(size_t i, cell m[MAXLEN + 1][MAXLEN + 1])
{
    m[0][i].cost = i;
    if (i > 0) {
        m[0][i].parent = INSERT;
    } else {
        m[0][i].parent = NO_PARENT;
    }
}

void column_init(size_t i, cell m[MAXLEN + 1][MAXLEN + 1])
{
    m[i][0].cost = i;
    if (i > 0) {
        m[i][0].parent = DELETE;
    } else {
        m[i][0].parent = NO_PARENT;
    }
}

size_t match(char c, char d)
{
    if (c == d) {
        return 0;
    } else {
        return 1;
    }
}

size_t indel(__attribute__((unused)) char c) { return 1; }

size_t swap(char c1, char c2, char d1, char d2)
{
    if (c1 == d2 && c2 == d1) {
        return 1;
    }
    return 2;
}

void goal_cell(const char *s, const char *t, size_t *i, size_t *j)
{
    *i = strlen(s);
    *j = strlen(t);
}

size_t string_compare(const char *s, const char *t,
                      cell m[MAXLEN + 1][MAXLEN + 1])
{
    size_t i, j, k;
    size_t opt[4];

    for (i = 0; i <= MAXLEN; i++) {
        row_init(i, m);
        column_init(i, m);
    }

    for (i = 1; i <= strlen(s); i++) {
        for (j = 1; j <= strlen(t); j++) {
            opt[MATCH] = m[i - 1][j - 1].cost + match(s[i - 1], t[j - 1]);
            opt[INSERT] = m[i][j - 1].cost + indel(t[j - 1]);
            opt[DELETE] = m[i - 1][j].cost + indel(s[i - 1]);
            if (i >= 2 && j >= 2) {
                opt[SWAP] = m[i - 2][j - 2].cost +
                            swap(s[i - 2], s[i - 1], t[j - 2], t[j - 1]);
            } else {
                opt[SWAP] = INT_MAX;
            }

            m[i][j].cost = opt[MATCH];
            m[i][j].parent = MATCH;
            for (k = INSERT; k <= SWAP; k++) {
                if (opt[k] < m[i][j].cost) {
                    m[i][j].cost = opt[k];
                    m[i][j].parent = k;
                }
            }
        }
    }

    goal_cell(s, t, &i, &j);
    return m[i][j].cost;
}

void match_out(const char *s, const char *t, size_t i, size_t j)
{
    if (s[i] == t[j]) {
        printf("M");
    } else {
        printf("S");
    }
}

void insert_out(__attribute__((unused)) const char *t,
                __attribute__((unused)) size_t j)
{
    printf("I");
}

void delete_out(__attribute__((unused)) const char *t,
                __attribute__((unused)) size_t j)
{
    printf("D");
}

void swap_out(__attribute__((unused)) const char *s,
              __attribute__((unused)) const char *t,
              __attribute__((unused)) size_t i,
              __attribute__((unused)) size_t j)
{
    printf("Sw");
}

void reconstruct_path(const char *s, const char *t, size_t i, size_t j,
                      cell m[MAXLEN + 1][MAXLEN + 1])
{
    if (m[i][j].parent == NO_PARENT) {
        return;
    }

    if (m[i][j].parent == MATCH) {
        reconstruct_path(s, t, i - 1, j - 1, m);
        match_out(s, t, i - 1, j - 1);
        return;
    }

    if (m[i][j].parent == INSERT) {
        reconstruct_path(s, t, i, j - 1, m);
        insert_out(t, j - 1);
        return;
    }

    if (m[i][j].parent == DELETE) {
        reconstruct_path(s, t, i - 1, j, m);
        delete_out(s, i - 1);
        return;
    }

    if (m[i][j].parent == SWAP) {
        reconstruct_path(s, t, i - 2, j - 2, m);
        swap_out(s, t, i - 1, j - 1);
        return;
    }
}

int main(int argc, char *argv[])
{
    cell m[MAXLEN + 1][MAXLEN + 1];

    if (argc < 3) {
        fprintf(stderr, "Usage: %s PATTERN TEXT\n", argv[0]);
        exit(1);
    }

    const char *s = argv[1];
    const char *t = argv[2];

    if (strlen(s) > MAXLEN) {
        fprintf(stderr, "Pattern string %s too long.\n", s);
        fprintf(stderr, "The maximum is %d characters. Exiting.\n", MAXLEN);
        exit(1);
    }

    if (strlen(t) > MAXLEN) {
        fprintf(stderr, "Text string %s too long.\n", t);
        fprintf(stderr, "The maximum is %d characters. Exiting.\n", MAXLEN);
        exit(1);
    }

    size_t cost = string_compare(s, t, m);
    printf("distance(%s, %s) = %zu\n", s, t, cost);

    size_t i, j;
    goal_cell(s, t, &i, &j);
    reconstruct_path(s, t, i, j, m);

    exit(0);
}
