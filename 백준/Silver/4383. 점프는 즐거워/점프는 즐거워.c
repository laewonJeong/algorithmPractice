#include <stdio.h>
#include <stdlib.h>
#define INPUT(x) scanf("%d", &x)

int main() {
    int  n, i;
    int  abs_diff;
    int *sequence;
    int *abs_diffs;

    while (INPUT(n) != EOF) {
        sequence  = malloc(sizeof(int) * n);
        abs_diffs = calloc(n, sizeof(int));

        for (i = 0; i < n; i++) {
            INPUT(sequence[i]);
            if (i > 0) {
                abs_diff = llabs(sequence[i] - sequence[i-1]);
                if (abs_diff > n - 1) {
                    continue;
                }
                abs_diffs[abs_diff] = 1; 
            }
        }

        for (i = 1; i < n; i++) {
            if (!abs_diffs[i]) {
                printf("Not jolly\n");
                goto clean;
            }
        }
        printf("Jolly\n");

      clean:
        free(abs_diffs);
        free(sequence);
    }

    return 0;
}