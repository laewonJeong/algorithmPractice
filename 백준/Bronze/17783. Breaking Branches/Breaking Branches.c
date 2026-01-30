#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    if (n % 2 == 1) {
        printf("Bob\n");
    } else {
        printf("Alice\n");
        printf("1\n");
    }

    return 0;
}