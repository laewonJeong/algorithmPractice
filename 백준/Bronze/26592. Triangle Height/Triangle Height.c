#include <stdio.h>
#define INPUT(x) scanf("%f", &x)

/* a = (h*b)/2  */
/* a * 2 / b = h*/
int main(void) {
    float a, b, h, n;

    INPUT(n);

    for (int i = 0; i < (int)n; i++) {
        INPUT(a);
        INPUT(b);

        h = (a * 2) / b;
        printf("The height of the triangle is %.2lf units\n", h);
    }

    return 0;
}