#include<stdio.h>
#include<iostream>
#include<vector>
#include<queue>
using namespace std;

int d[10002];
void dijkstra(vector<pair<int,int>> *graph, int start, int n) {
	for (int i = 0; i <= n; i++) {
		d[i] = 987654321;
	}
	d[start] = 0;
	priority_queue<pair<int, int>> pq;
	pq.push(make_pair(0, start));
	while (!pq.empty()) {
		int current = pq.top().second;
		int distance = -pq.top().first;
		pq.pop();
		if (d[current] < distance)
			continue;
		for (int i = 0; i < graph[current].size(); i++) {
			int next = graph[current][i].first;
			if (distance + graph[current][i].second < d[next]) {
				d[next] = distance + graph[current][i].second;
				pq.push(make_pair(-(distance + graph[current][i].second), next));
			}
		}
	}
}
int main() {
	int testcase;
	int n, de, c;
	int a, b, s;
	int max = 0;
	int cnt = 0;
	cin >> testcase;

	while (testcase--) {
		vector<pair<int, int>> graph[10002];
		cin >> n >> de>> c;
		for (int i = 0; i < de; i++) {
			cin >> a >> b >> s;
			graph[b].push_back(make_pair(a, s));
		}
		dijkstra(graph,c,n);
		for (int i = 0; i <= n; i++) {
			if (d[i] != 987654321 && max < d[i])
				max = d[i];
			if (d[i] != 987654321) {
				cnt++;
			}
		}
		cout << cnt << " " << max<<"\n";
		cnt = 0;
		max = 0;
	}
}