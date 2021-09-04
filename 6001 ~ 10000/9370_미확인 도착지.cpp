#include<stdio.h>
#include<iostream>
#include<cstring>
#include <queue>
#include<vector>
#include<algorithm>
#define INF 987654321
using namespace std;
int d[2002];
void dijkstra(vector<pair<int,int>> *graph, int start, int vertex) {
    for (int i = 1; i <= vertex; i++)
        d[i] = INF;
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
    int te;
    int n, m, t;
    int c, g, h;
    int s, de, w;
    int temp;
    int compare_a, compare_b, compare_c, compare_d, compare_e, compare_f;
    vector<int> bench;
    cin >> te;
    while (te--) {
        vector<pair<int, int>> graph[2002];
        cin >> n >> m >> t;
        cin >> c >> g >> h;
        for (int i = 0; i < m; i++) {
            cin >> s >> de >> w;
            graph[s].push_back(make_pair(de, w));
            graph[de].push_back(make_pair(s, w));
        }
        for (int i = 0; i < t; i++) {
            cin >> temp;
            dijkstra(graph,c,n);
            compare_a = d[temp];
            compare_b = d[g];
            compare_e = d[h];
            dijkstra(graph, g, n);
            compare_c = d[h];
            dijkstra(graph, h, n);
            compare_d = d[temp];
            if (compare_a == compare_b + compare_c + compare_d) {
                bench.push_back(temp);
                continue;
            }
            dijkstra(graph, h, n);
            compare_f = d[g];
            dijkstra(graph, g, n);
            compare_d = d[temp];
            if (compare_a == compare_e + compare_f + compare_d) {
                bench.push_back(temp);
            }
            
        }
        sort(bench.begin(),bench.end());
        for (int i = 0; i < bench.size(); i++) {
            cout << bench[i] << " ";
        }
        cout << "\n";
        bench.clear();
    }

}