#include <stdio.h>
#define INPUT(x) scanf("%d", &x)
#define PI 3.141592

int main() {
    int d1, d2;

    INPUT(d1);
    INPUT(d2);

    printf("%lf\n", 2 * d1 + (2 * d2 * PI));

    return 0;
}