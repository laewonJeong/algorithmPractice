#include <stdio.h>
#include <string.h>
#define INPUT(...) scanf(__VA_ARGS__)
#define PRINT(...) printf(__VA_ARGS__)
#define SEMINAR_CNT 7

int main() {
    // Write your solution here
    int i;
    int max;
    int applicant;
    char seminar[30];
    char answer[30];

    max = 0;
    for (i = 0; i < SEMINAR_CNT; i++) {
        INPUT("%s", seminar);
        INPUT("%d\n", &applicant);

        if (applicant > max) {
            max = applicant;
            strcpy(answer, seminar);
        }
    }

    PRINT("%s\n", answer);

    return 0;
}