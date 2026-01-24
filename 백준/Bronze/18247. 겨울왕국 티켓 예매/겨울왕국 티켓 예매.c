#include <stdio.h>
#include <limits.h>
#define INPUT(x) scanf("%d", &x)

int main(void) {
    int t, i, n, m;

    INPUT(t);

    for (i = 0; i < t; i++) {
        INPUT(n);
        INPUT(m);

        if (n < 12 || m < 4) {
            printf("-1\n");
            continue;
        }

        printf("%d\n", m * 11 + 4);
    }

    return 0;
}