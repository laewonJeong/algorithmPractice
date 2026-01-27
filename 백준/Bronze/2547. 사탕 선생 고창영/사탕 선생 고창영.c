#include <stdio.h>

int main() {
    int t, n;
    unsigned long long candy;

    scanf("%d", &t);

    while (t--) {
        scanf("%d", &n);

        unsigned long long candies = 0;

        for (int i = 0; i < n; i++) {
            scanf("%llu", &candy);
            candies = (candies + candy) % n;
        }

        if (candies == 0)
            printf("YES\n");
        else
            printf("NO\n");
    }

    return 0;
}