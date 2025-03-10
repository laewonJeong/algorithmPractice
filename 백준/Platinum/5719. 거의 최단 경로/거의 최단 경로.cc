#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstring>
#include <map>
#define INF 987654321
using namespace std;

int v, e;
int source, destination;
vector<int> d(502);
map<int, int> graph[502];
vector <int> trace[502];
vector<bool> visited(502);
void del_node(int end) {
	if (end == source) return;

	if (visited[end]) return;
	visited[end] = true;

	for (int i = 0; i < trace[end].size(); i++) {
		int next = trace[end][i];
		graph[next][end] = -1;
		del_node(trace[end][i]);
	}
}
void dijkstra() {
	for (int i = 0; i < v; i++) {
		d[i] = INF;
	}
	d[source] = 0;
	priority_queue<pair<int, int>> pq;
	pq.emplace(0,source);
	while (!pq.empty()) {
		int current = pq.top().second;
		int distance = -pq.top().first;
		pq.pop();
		
		if (d[current] < distance)
			continue;
		for (auto x: graph[current]) {
			int next = x.first;
			int ncost = x.second;
			if (ncost == -1) {
				continue;
			}
			if (d[next] > d[current] + ncost) {
				trace[next].clear();
				trace[next].emplace_back(current);
				d[next] = d[current] + ncost;
				pq.emplace(-d[next], next);
			}
			else if (d[next] == d[current] + ncost) 
				trace[next].emplace_back(current);
		}
	}
}

int main() {

	while (1) {
		cin >> v >> e;
		if (v == 0 && e == 0) {
			break;
		}
		cin >> source >> destination;
		for (int i = 0; i < 502; i++) {
			graph[i].clear();
			trace[i].clear();
			visited[i] = false;
		}
		for (int i = 0; i < e; i++) {
			int s, de, w;
			cin >> s >> de >> w;
			graph[s][de] = w;
		}
		dijkstra();
		del_node(destination);
		dijkstra();
		if (d[destination] == INF)
			cout << -1 << "\n";
		else
			cout << d[destination] << "\n";
	}
}