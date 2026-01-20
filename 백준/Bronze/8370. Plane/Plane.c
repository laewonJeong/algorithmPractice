#include <stdio.h>
#define INPUT(x) scanf("%d", &x)

int main() {
  int n1, k1, n2, k2;

  INPUT(n1);
  INPUT(k1);
  INPUT(n2);
  INPUT(k2);

  printf("%d\n", n1 * k1 + n2 * k2);

  return 0;
}