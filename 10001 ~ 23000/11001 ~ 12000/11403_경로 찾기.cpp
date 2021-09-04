#include<stdio.h>
#include<iostream>
using namespace std;
int graph[102][102];
void Floyd(int v) {
	for (int k = 0; k < v; k++) 
		for (int i = 0; i < v; i++)  
			for (int j = 0; j < v; j++)  
				if (graph[i][k] + graph[k][j] < graph[i][j])  
					graph[i][j] = graph[i][k] + graph[k][j];
}
int main() {
	int num;
	int x;
	cin >> num;
	for (int i = 0; i < num; i++) {
		for (int j = 0; j < num; j++) {
			cin >> x;
			if (x == 0)
				graph[i][j] = 987654321;
			else
				graph[i][j] = x;
		}
	}
	Floyd(num);
	for (int i = 0; i < num; i++) {
		for (int j = 0; j < num; j++) {
			if (graph[i][j] == 987654321)
				cout << 0 << " ";
			else
				cout << 1<< " ";
		}
		cout << "\n";
	}
}