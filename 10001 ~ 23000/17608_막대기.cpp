#include<stdio.h>
#include<iostream>
#include<stack>
#include <vector>

using namespace std;
int main() {
	int n;
	stack<int> s;
	int x;
	int max = 0;
	int cnt = 0;
	cin >> n;
	while (n--) {
		cin >> x;
		s.push(x);
	}
	while (!s.empty()) {
		if (max < s.top()) {
			max = s.top();
			cnt++;
		}
		s.pop();
	}
	cout << cnt;
}