#include <stdio.h>
#define INPUT(x) scanf("%d", &x)

int main() {
  while (1) {
    int boys, girls;
    INPUT(boys);
    INPUT(girls);

    if (!boys && !girls) {
      break;
    }

    printf("%d\n", boys + girls);
  }

  return 0;
}