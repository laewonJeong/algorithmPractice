#include <stdio.h>
#define INPUT(x) scanf("%d", &x)

int main(void) {
    int n, i, a;

    INPUT(n);

    for (i = 0; i < n; i++){
        INPUT(a);

        printf("%d %d\n", a, a);
    }

    return 0;
}