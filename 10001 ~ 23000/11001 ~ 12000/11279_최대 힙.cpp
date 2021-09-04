#include<iostream>
#include<queue>

using namespace std;

int main() {
	int n;
	int c;
	scanf("%d", &n);
	priority_queue<int> pq;
	for (int i = 0; i < n; i++) {
		scanf("%d", &c);
		if (c == 0) {
			if (pq.empty())
				printf("0\n");
			else {
				printf("%d\n", pq.top());
				pq.pop();
			}
		}
		else
			pq.push(c);
	}
}