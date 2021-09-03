#include<stdio.h>
#include<iostream>
#include<cstdio>
#include<stack>
#include<vector>
#include<math.h>
#include<string.h>
#include<string>
#include<queue>
using namespace std;
int n, m;
int arr[1001][1001] = { 0, };
int dcheck[1001] = { 0, };
int bcheck[1001] = { 0, };
int cnt = 0;
int dfs(int v) {
	cnt++;
	dcheck[v] = 1;
	for (int i = 1; i <= n; i++) {
		if (dcheck[i] == 1 || arr[v][i] == 0)
			continue;
		dfs(i);
	}
	return cnt;
}
int main(void) {
	cin >> n >> m;
	int x, y;
	for (int i = 1; i <= m; i++) {
		cin >> x >> y;
		arr[x][y] = 1;
		arr[y][x] = 1;
	}
	cout << dfs(1)-1;
}