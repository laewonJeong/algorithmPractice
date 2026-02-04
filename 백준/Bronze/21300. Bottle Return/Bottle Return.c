#include <stdio.h>
#define INPUT(x) scanf("%d", &x)

int main() {
    // Write your solution here
    int i;
    int empty;
    int answer;

    answer = 0;
    for (i = 0; i < 6; i++) {
        INPUT(empty);
        answer += empty * 5;
    }

    printf("%d\n", answer);

    return 0;
}