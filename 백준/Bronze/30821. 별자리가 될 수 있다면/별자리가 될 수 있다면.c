#include <stdio.h>

int main() {
    // Write your solution here
    long long n, result;

    scanf("%lld", &n);

    if (n < 5) {
        result = 0;
    } else {
        result = n * (n - 1) * (n - 2) * (n - 3) * (n - 4) / 120;
    }

    printf("%lld\n", result);

    return 0;
}