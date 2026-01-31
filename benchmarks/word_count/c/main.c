#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_WORDS 1024
// Simple Hash Map
typedef struct {
    char *key;
    int count;
} Entry;

Entry table[MAX_WORDS];

unsigned long hash(const char *str) {
    unsigned long hash = 5381;
    int c;
    while ((c = *str++))
        hash = ((hash << 5) + hash) + c; /* hash * 33 + c */
    return hash;
}

void add_word(const char *word) {
    unsigned long h = hash(word);
    int idx = h % MAX_WORDS;
    
    while (table[idx].key != NULL) {
        if (strcmp(table[idx].key, word) == 0) {
            table[idx].count++;
            return;
        }
        idx = (idx + 1) % MAX_WORDS;
    }
    
    // New entry
    table[idx].key = strdup(word);
    table[idx].count = 1;
}

int main() {
    FILE *f = fopen("../../data/input.txt", "r");
    if (!f) {
        fprintf(stderr, "Failed to open input.txt\n");
        return 1;
    }

    char buffer[256];
    while (fscanf(f, "%255s", buffer) == 1) {
        add_word(buffer);
    }
    
    fclose(f);

    int unique = 0;
    for (int i = 0; i < MAX_WORDS; i++) {
        if (table[i].key) unique++;
    }
    
    printf("Unique words: %d\n", unique);
    return 0;
}
