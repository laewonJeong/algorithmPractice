#include <stdio.h>
#define INPUT(x) scanf("%d", &x)
#define PRINT(...) printf(__VA_ARGS__)

int main() {
    // Write your solution here
    int my_money;
    int parent_money;

    INPUT(my_money);

    if (my_money >= 1000000) {
        parent_money = my_money * 0.2;
    } else if (my_money >= 500000) {
        parent_money = my_money * 0.15;
    } else if (my_money >= 100000) {
        parent_money = my_money * 0.1;
    } else {
        parent_money = my_money * 0.05;
    }

    my_money -= parent_money;

    PRINT("%d %d\n", parent_money, my_money);

    return 0;
}