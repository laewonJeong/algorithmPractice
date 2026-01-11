#include <stdio.h>
#include <string.h>
#include <ctype.h>
int main(void)
{
	int i, j, n, x,y, m,o, len, lenn;
	int k = 0;
	char a[21];
	char temp[21];
	char temp1[21];
	char temp2[21];

	while (1) {
		scanf("%d", &n);
		if (n == 0)
			break;
		else {
			for (i = 0; i < n; i++) {
				scanf("%s", a);
				len = strlen(a);
				for (x = 0; x < len; x++)
					temp1[x] = a[x];
				for (y = 0; y < len; y++) {
						a[y] = tolower(a[y]);
				}
				for (j = 0; j < len; j++) {
					if (k == 0) {
						for (m = 0; m < len; m++) {
							temp[m] = a[m];
							temp2[m] = temp1[m];
						}
						lenn = len;
						break;
					}
					else if (a[j] > temp[j]) {
						break;
					}
					else if (a[j] < temp[j]) {
						for (o = 0; o < len; o++) {
							temp[o] = a[o];
							temp2[o] = temp1[o];
						}
						lenn = len;
						break;
					}
					else if (a[j] == temp[j]) {
						if (a[j + 1] == '\0' && temp[j + 1] != '\0') {
							for (o = 0; o < len; o++) {
								temp[o] = a[o];
								temp2[o] = temp1[o];
							}
							lenn = len;
						}
						else
							continue;
					}
				}
				k = 1;
			}
		}
		for (j = 0; j<lenn; j++)
			printf("%c", temp2[j]);
		k = 0;
		printf("\n");
	}
	return 0;
}