#include<stdio.h>
#include<iostream>
#include<stack>
#include <vector>
#include <algorithm>
#include<math.h>
using namespace std;
int main() {
	int n;
	int x, y;
	long double a = 0;
	long double b = 0;
	long double result;
	cin >> n;
	vector<pair<double, double>> arr;
	for (int i = 0; i < n; i++) {
		cin >> x >> y;
		arr.push_back(make_pair(x, y));
	}
	arr.push_back(make_pair(arr[0].first, arr[0].second));
	for (int i = 0; i < n; i++) {
		a += arr[i].first * arr[i + 1].second;
	}
	for (int i = 0; i < n; i++) {
		b += arr[i].second * arr[i + 1].first;
	}
	result = fabs(a - b)/2;
	cout.setf(ios::fixed);
	cout.precision(1);
	cout << result;
	return 0;
}