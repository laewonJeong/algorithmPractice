#include <stdio.h>
#define INPUT(x) scanf("%d", &x)

int main(void) {
    int t;
    int n, m;
    int temp;

    INPUT(t);

    for (int i = 0; i < t; i++) {
        INPUT(n);
        INPUT(m);

        for (int j = 0; j < n; j++) {
            INPUT(temp);
        }

        for (int j = 0; j < m; j++) {
            INPUT(temp);
        }

        if (n <= m) {
            printf("Yes\n");
        } else {
            printf("No\n");
        }
    }

    return 0;
}