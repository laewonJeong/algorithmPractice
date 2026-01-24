#include <stdio.h>
#include <limits.h>
#define INPUT(x) scanf("%d", &x)
#define MAX(a, b) (a) > (b) ? (a) : (b)

int main(void) {
    int n, i, j, temp;
    int max;
    INPUT(n);

    for (i = 0; i < n; i ++) {
        max = -INT_MAX;

        for (j = 0; j < 5; j++) {
            INPUT(temp);
            max = MAX(max, temp);
        }

        printf("Case #%d: %d\n", i + 1, max);

    }

    return 0;
}