#include<stdio.h>
#include<iostream>
#include<cstring>
#define INF 987654321
using namespace std;
long long graph[102][102];
void Floyd(int v){
    for (int mid=1;mid<=v;mid++){
        for (int start=1;start<=v;start++){
            for (int end=1;end<=v;end++){
                if (graph[start][end] > graph[start][mid] + graph[mid][end]){
                    graph[start][end] = graph[start][mid] + graph[mid][end];
                }
            }
        }
    }
}
int main() {
    int v;
    int e;
    int s, d, w;
    cin >> v >> e;
    for(int i=1;i<=v;i++){
        for(int j=1;j<=v;j++){
            if(i==j)
                graph[i][j]=0;
            else
              graph[i][j] = INF;
        }
    }
    for (int i = 0; i < e; i++) {
        cin >> s >> d >> w;
        if(graph[s][d]!=-1 && graph[s][d]<w)
            continue;
        graph[s][d] = w;
    }
    Floyd(v);
    for(int i=1;i < v+1; i++){
        for(int j=1; j < v+1; j++){
            if(graph[i][j] == INF)
                cout << 0 <<" ";
            else
                cout<< graph[i][j]<<" ";
        }
        cout << "\n";
    }
}