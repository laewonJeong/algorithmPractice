#include<stdio.h>
#include<iostream>
#include<queue>
#include <vector>
#define INF 987654321
using namespace std;

int main() {
	priority_queue<int> pq;
	int result=0;
	int temp;
	int testcase;
	int card;
	int a, b;
	scanf("%d", &testcase);
	while (testcase--) {
		scanf("%d", &card);
		pq.push(-card);
	}
	if (testcase == 1) {
		cout << pq.top();
	}
	else {
		while (pq.size()>1) {
			a = -pq.top();
			pq.pop();
			b = -pq.top();
			pq.pop();
			result += a + b;
			pq.push(-(a + b));
		}
		printf("%d", result);
	}
}