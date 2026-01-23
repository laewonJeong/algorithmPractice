/* 삼각 김밥 */
#include <stdio.h>
#include <float.h>
#define INPUT(x) scanf("%d", &x)
#define MIN(a, b) (a) < (b) ? (a) : (b)

double price_per_1000(int price, int gram) {
    return (price / (double)gram) * 1000.0;
}

int main() {
    /* Write your solution here */
    int     n, i;
    int     price, gram;
    double  min;

    INPUT(price);
    INPUT(gram);

    min = price_per_1000(price, gram);

    INPUT(n);

    for (i = 0; i < n; i++) {
        INPUT(price);
        INPUT(gram);

        min = MIN(min, (double)price_per_1000(price, gram));
    }

    printf("%.2lf", min);

    return 0;
}