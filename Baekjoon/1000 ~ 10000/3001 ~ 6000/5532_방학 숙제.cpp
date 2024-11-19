#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;
int main(){
	double l,a,b,c,d;
	cin >> l >> a >> b >> c >> d;
	cout << l-max(ceil(a/c),ceil(b/d)) << endl;
}
