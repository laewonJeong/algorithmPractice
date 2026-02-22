#include <stdio.h>
#define INPUT(x) scanf("%d", &x);
#define MAX(a, b) a > b ? a : b
#define MIN(a, b) a < b ? a : b

int main() {
    // Write your solution here
    int arr[3];
    int i;
    int max;
    int min;

    max = 0;
    min = 101;

    for (i = 0; i < 3; i++) {
        INPUT(arr[i]);
        max = MAX(max, arr[i]);
        min = MIN(min, arr[i]);
    }

    for (i = 0; i < 3; i++) {
        if (arr[i] != max && arr[i] != min) {
            printf("%d\n", arr[i]);
            return 0;
        }
    }

    return 0;
}