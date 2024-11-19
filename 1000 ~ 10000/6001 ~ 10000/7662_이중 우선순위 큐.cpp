#include<iostream>
#include<cstdio>
#include<set>

using namespace std;

int main() {
	int testcase;
	multiset<long long> ms;
	cin >> testcase;
	for (int i = 0; i < testcase; i++) {
		int number;
		cin >> number;
		for (int j = 0; j < number; j++) {
			char cmd;
			int num;
			cin >> cmd >> num;
			if (cmd == 'I') {
				ms.insert(num);
			}
			else if (cmd == 'D' && ms.size()>0) {
				if (num == 1) {
					auto temp = ms.end();
					temp--;
					ms.erase(temp);
				}
				else if (num == -1) {
					ms.erase(ms.begin());
				}
			}
		}
		if (ms.empty())
			cout << "EMPTY" << "\n";
		else {
			auto max = ms.end();
			max--;
			cout << *max << ' '<< *ms.begin()<< "\n";
		}
		ms.clear();
	}
}