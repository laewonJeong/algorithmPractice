#include<iostream>
#include<algorithm>

using namespace std;


int main() {
	int max = -10000000;
	int row, col;
	int i, j;
	int x;
	for (i = 1; i < 10; i++) {
		for (j = 1; j < 10; j++) {
			cin >> x;
			if (max < x) {
				max = x;
				row = i;
				col = j;
			}
		}
	}

	cout << max << "\n";
	cout << row << " " << col;
}