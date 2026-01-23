/* Transactions */
#include <stdio.h>
#define LIMIT -200

int main() {
    // Write your solution here
    int     a, b;
    char    c;

    while (1){
        scanf("%d %c %d", &a, &c, &b);

        if (a == 0 && c == 'W' && b == 0){
            break;
        }

        if (c == 'D') {
            printf("%d\n", a + b);
            continue;
        }

        /* 여기 까지 온거면 c는 W다. */
        if (a - b >= LIMIT) {
            printf("%d\n", a - b);
        } else {
            printf("Not allowed\n");
        }

    }

    return 0;
}