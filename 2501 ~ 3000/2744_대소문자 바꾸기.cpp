#include<iostream>
#include<string.h>
#include<algorithm>

using namespace std;

int main() {
	char s[102];
	cin >> s;
	for (int i = 0; i < strlen(s); i++) {
		if (s[i] >= 'A' && s[i] <= 'Z')
			s[i] += 32;
		else
			s[i] -= 32;
	}
	cout << s << "\n";
}