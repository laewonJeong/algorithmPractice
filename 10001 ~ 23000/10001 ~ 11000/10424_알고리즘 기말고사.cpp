#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
vector<pair<int,int>> student;
int main() {
	int num;
	int x;
	int bi, ci;
	int high_fin=0;
	int low_fin=0;
	scanf("%d",&num);
	for (int i = 1; i <= num; i++) {
		scanf("%d",&x);
		student.push_back(make_pair(x,i));
	}
	sort(student.begin(), student.end());
	for (int i = 0; i < num; i++) {
		printf("%d\n", student[i].first - student[i].second);
	}
}