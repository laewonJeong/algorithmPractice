#include <stdio.h>
#define INPUT(x) scanf("%d", &x)

int main() {
    int t, i;
    int cnt;
    int answer;

    INPUT(t);

    cnt = 0;
    for (i = 0; i < 5; i++) {
        INPUT(answer);
        if (answer == t) {
            cnt++;
        }
    }

    printf("%d\n", cnt);
}