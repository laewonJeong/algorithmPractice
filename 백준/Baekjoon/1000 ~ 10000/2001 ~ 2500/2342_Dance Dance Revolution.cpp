#include<stdio.h>
#include<iostream>
#include<stack>
#include <vector>
#include <algorithm>
#include<math.h>
#include<cstring>
using namespace std;
int arr[100001];
int DP[100001][5][5];
int n = 0;
int foot(int start, int end) {
	if (start == 0)
		return 2;
	else if (start == end)
		return 1;
	else if (abs(start - end) == 2)
		return 4;
	else
		return 3;
}
int dp(int idx, int left, int right) {
	if (idx == n + 1)
		return 0;
	int& result = DP[idx][left][right];
	if (result != -1)
		return result;
	result = min(dp(idx + 1, arr[idx], right) + foot(left, arr[idx]), dp(idx + 1, left, arr[idx]) + foot(right, arr[idx]));
	return result;
}

int main() {
	int x;
	while(true) {
		scanf("%d", &x);
		if (x == 0)
			break;
		n++;
		arr[n] = x;
	}
	memset(DP, -1, sizeof(DP));
	printf("%d", dp(1, 0, 0));
}