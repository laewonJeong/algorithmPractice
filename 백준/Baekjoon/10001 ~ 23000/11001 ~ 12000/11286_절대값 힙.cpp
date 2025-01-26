#include<stdio.h>
#include<iostream>
#include<cstring>
#include <queue>
using namespace std;
int main() {
	priority_queue<pair<int,int>> pq;
	int t;
	int x;
	int y;
	scanf("%d",&t);
	while (t--) {
		scanf("%d",&x);
		if (x != 0)
			pq.push(make_pair(-abs(x), -x));
		else {
			if (pq.empty())
				printf("0\n");
			else {
				y = pq.top().second;
				pq.pop();
				printf("%d\n", -y);
			}
		}
	}
}