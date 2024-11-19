#include<iostream>
#include<string.h>
#include<algorithm>

using namespace std;

int main() {
	double n;
	double money;
	cin >> n;
	while (n != 0) {
		cin >> money;
		printf("$%.2f\n", money*0.8);
		n--;
	}
}
