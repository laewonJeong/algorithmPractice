#include <stdio.h>
#define INPUT(x) scanf("%d", &x)

int main() {
  int x, n, a, b, i;
  int price = 0;

  INPUT(x);
  INPUT(n);

  for (i = 0; i < n; i++){
    INPUT(a);
    INPUT(b);

    price += a * b;
  }

  if (x == price){
    printf("Yes\n");
  } else {
    printf("No\n");
  }

  return 0;
}