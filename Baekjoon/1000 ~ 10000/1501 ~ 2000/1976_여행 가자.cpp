#include<stdio.h>
#include<iostream>
#include<string.h>
#include<stack>
#include <vector>
#define INF 987654321
using namespace std;
int graph[202][202];
void Floyd(int v) {
	for (int k = 1; k < v+1; k++) {
		for (int i = 1; i < v+1; i++) {
			for (int j = 1; j < v+1; j++) {
				if (graph[i][k]==1 && graph[k][j]==1)
					graph[i][j] = 1;
			}
		}
	}
}
int main() {
	int city;
	int tp;
	vector<int>travelplan;
	int x;
	int check = 1;
	scanf("%d", &city);
	scanf("%d", &tp);
	for (int i = 1; i < city+1; i++) {
		for (int j = 1; j < city+1; j++) {
			scanf("%d", &x);
			graph[i][j] = x;
			graph[i][i] = 1;
		}
	}
	for (int i = 0; i < tp; i++) {
		scanf("%d", &x);
		travelplan.push_back(x);
	}
	Floyd(city);
	for (int i = 0; i < travelplan.size()-1; i++) {
		if (graph[travelplan[i]][travelplan[i + 1]] != 1 && graph[travelplan[i+1]][travelplan[i]] != 1) {
			check = 0;
			break;
		}
	}
	if (check == 1) 
		printf("YES");
	else {
		printf("NO");
	}
}