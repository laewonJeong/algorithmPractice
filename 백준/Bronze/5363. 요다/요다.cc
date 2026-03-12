#include <stdio.h>
#include <string.h>
#define INT_INPUT(x) scanf("%d\n", &x)
#define INPUT(x) fgets(x, sizeof(x), stdin)


int main() {
    int   n, i;
    char  line[102];
    char *first;
    char *second;
    char *after;

    INT_INPUT(n);

    for (i = 0; i < n; i++) {
        INPUT(line);

        first  = strtok(line, " ");
        second = strtok(NULL, " ");
        after  = strtok(NULL, "\n");

        printf("%s %s %s\n", after, first, second);
    }

    return 0;
}