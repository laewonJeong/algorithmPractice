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
int n, m, v;
int arr[1001][1001] = { 0, };
int dcheck[1001] = { 0, };
int bcheck[1001] = { 0, };

void dfs(int v) {
	cout << v<< " ";
	dcheck[v] = 1;
	for (int i = 1; i <= n; i++) {
		if (dcheck[i] == 1 || arr[v][i] == 0)
			continue;
		dfs(i);
	}
}
void bfs(int v) {
	queue<int> q;
	bcheck[v] = 1;
	q.push(v);
	while (!q.empty()) {
		v = q.front();
		cout << v << " ";
		q.pop();
		for (int i = 1; i <= n; i++) {
			if (bcheck[i] == 1 || arr[v][i] == 0)
				continue;
			q.push(i);
			bcheck[i] = 1;
		}

	}
}
int main(void) {
	cin >> n >> m >> v;
	int x, y;
	for (int i = 1; i <= m; i++) {
		cin >> x >> y;
		arr[x][y] = 1;
		arr[y][x] = arr[x][y];
	}
	dfs(v);
	cout << "\n";
	bfs(v);

}