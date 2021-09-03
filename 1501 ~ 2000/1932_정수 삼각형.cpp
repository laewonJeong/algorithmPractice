#include<iostream>
#include<algorithm>

using namespace std;

int main() {
	int n;
	cin >> n;
	int arr[501][501] = { 0, };
	int dp[501][501] = { 0, };
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= i; j++) {
			cin >> arr[i][j];
		}
	}
	dp[1][1] = arr[1][1];
	for (int i = 2; i <= n; i++) {
		for (int j = 1; j <= i; j++) {
			dp[i][j] = arr[i][j] + max(dp[i - 1][j - 1], dp[i - 1][j]);
		}
	}
	int max = arr[1][1];
	for (int j = 1; j <= n; j++) {
		if (dp[n][j] >= max)
			max = dp[n][j];
	}
	cout << max;
	return 0;
}