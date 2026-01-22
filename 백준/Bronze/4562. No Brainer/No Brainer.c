#include <stdio.h>
#define INPUT(x) scanf("%d", &x)

int main(void) {
    int n, i, a, b;

    INPUT(n);

    for (i = 0; i < n; i++){
        INPUT(a);
        INPUT(b);

        if (a - b < 0) {
            printf("NO BRAINS\n");
        } else {
            printf("MMM BRAINS\n");
        }
    }

    return 0;
}