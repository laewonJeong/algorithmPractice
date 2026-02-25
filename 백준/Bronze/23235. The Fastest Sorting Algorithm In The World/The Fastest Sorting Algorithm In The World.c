#include <stdio.h>
#define INPUT(x) scanf("%d", &x)

int main() {
    // Write your solution here
    int cnt, num;
    int c, i;

    c = 0;
    while (1) {
        INPUT(cnt);
        if (!cnt){
            break;
        }

        for (i = 0; i < cnt; i++) {
            INPUT(num);
        }

        printf("Case %d: Sorting... done!\n", ++c);
    }

    return 0;
}