#include <stdio.h>
#define INPUT(x) scanf("%d", &x)
#define PRINT(x) printf("%s\n", x)
#define HAPPYNESS_SCORE(s, m, l) 1 * (s) + 2 * (m) + 3 * (l)

int main() {
    // Write your solution here
    int s, m, l;

    INPUT(s);
    INPUT(m);
    INPUT(l);

    PRINT(HAPPYNESS_SCORE(s, m, l) >= 10 ? "happy" : "sad");

    return 0;
}