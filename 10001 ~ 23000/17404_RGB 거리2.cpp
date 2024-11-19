#include<stdio.h>
#include<iostream>
#include<stack>
#include <vector>
#include <algorithm>
#define INF 987654321
using namespace std;
int main() {
	int home;
	cin >> home;
	int rgb[1001][3];
	int r, g, b;
	int result = INF;
	for (int i = 0; i < home; i++) {
		cin >> r >> g >> b;
		rgb[i][0] = r;
		rgb[i][1] = g;
		rgb[i][2] = b;
	}
	for (int i = 0; i < 3; i++) {
		int dp[1001][3];
		for (int j = 0; j < 3; j++) {
			if (i == j) {
				dp[0][j] = rgb[0][j];
				continue;
			}
			dp[0][j] = INF;
		}
		for (int j = 1; j < home; j++) {
			dp[j][0] = rgb[j][0] + min(dp[j - 1][1], dp[j - 1][2]);
			dp[j][1] = rgb[j][1] + min(dp[j - 1][0], dp[j - 1][2]);
			dp[j][2] = rgb[j][2] + min(dp[j - 1][0], dp[j - 1][1]);
		}
		for (int j = 0; j < 3; j++) {
			if (j == i)
				continue;
			result = min(result, dp[home - 1][j]);
		}
	}
	cout << result;
}