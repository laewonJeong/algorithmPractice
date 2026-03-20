#include <iostream>
#include <string>
#include <set>

using namespace std;

int main() {
    int n, i;
    int week;
    string city;

    week = 1;
    while (week++) {
        cin >> n;
        cin.ignore();
        if (!n) break;

        set<string> s;
        for (i = 0; i < n; i++) {
            getline(cin, city);
            s.insert(city);
        }

        cout << "Week " << week - 1 << " " << s.size() << endl;
    }

    return 0;
}