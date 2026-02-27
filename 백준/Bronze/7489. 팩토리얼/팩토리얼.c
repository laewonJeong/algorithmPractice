#include <stdio.h>
#define INPUT(x) scanf("%d", &x)

int main() {
    int t, n;
    int i, j;

    INPUT(t);

    while (t--) {
        INPUT(n);

        long long result = 1;

        for (i = 2; i <= n; i++) {
            result *= i;

            while (result % 10 == 0)
                result /= 10;

            result %= 100000;
        }

        printf("%lld\n", result % 10);
    }

    return 0;
}