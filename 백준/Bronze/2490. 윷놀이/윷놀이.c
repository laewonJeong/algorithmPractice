#include <stdio.h>
#define INPUT(x) scanf("%d", &x)

char yut_result(int yut) {
    char result;

    switch (yut){
    case 0:
        result = 'D';
        break;
    case 1:
        result = 'C';
        break;
    case 2:
        result = 'B';
        break;
    case 3:
        result = 'A';
        break;
    case 4:
        result = 'E';
        break;
    }

    return result;
}

int main() {
    // Write your solution here
    int i, j, temp;
    int yut;

    for (i = 0; i < 3; i++) {
        yut = 0;
        for (j = 0; j < 4; j++) {
            INPUT(temp);
            yut += temp;
        }

        printf("%c\n", yut_result(yut));
    }
    return 0;
}