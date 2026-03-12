#include <stdio.h>
#include <string.h>

int main() {
    int n, i;
    char first[102];
    char second[102];
    char after[102];

    scanf("%d\n", &n);

    for (i = 0; i < n; i++) {
        scanf("%s", first);
        scanf("%s ", second);
        fgets(after, sizeof(after), stdin);
        after[strlen(after)-1] = '\0';

        printf("%s %s %s\n", after, first, second);
    }

    return 0;
}