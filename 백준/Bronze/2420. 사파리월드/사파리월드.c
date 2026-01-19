#include <stdio.h>
#include <stdlib.h>
#define INPUT(x) scanf("%lld", &x)

int main() {
  long long n, m;

  INPUT(n);
  INPUT(m);

  printf("%lld\n", llabs(n - m));

  return 0;
}