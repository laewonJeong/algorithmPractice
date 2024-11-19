#include<stdio.h>
#include<iostream>
#include<stack>
#include <vector>

using namespace std;
int main() {
	int n;
	stack<pair<int,int>> s;
	int x;
	scanf("%d", &n);
	for(int i=1;i<n+1;i++){
		scanf("%d", &x);
		if (i == 1)
			cout << 0 <<" ";
		else {
			while (!s.empty()) {
				if (s.top().first > x) {
					break;
				}
				s.pop();
			}
			if (s.empty())
				printf("0 ");
			else
				printf("%d ", s.top().second);
		}
		s.push(make_pair(x, i));
	}
}