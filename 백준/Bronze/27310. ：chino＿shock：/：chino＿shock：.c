#include <stdio.h>
#include <string.h>

#define LEN(x)              strlen(x)
#define INPUT(x)            scanf("%s", x)
#define PRINT(x)            printf("%d\n", x)
#define DIFFICULTY(x, y, z) (x) + (y) + (z) * 5

int main() {
    // Write your solution here
    int  i;
    int  len;
    int  colon;
    int  under_bar;
    char emoji[33];

    INPUT(emoji);

    len = LEN(emoji);

    colon = under_bar = 0;
    for (i = 0; i < len; i++) {
        if (emoji[i] == ':') {
            colon++;
        } else if (emoji[i] == '_') {
            under_bar++;
        } else {
            /* nothing to do */
        }
    }

    PRINT(DIFFICULTY(len, colon, under_bar));

    return 0;
}