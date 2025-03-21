#include <bits/stdc++.h>
using namespace std;

const int N = 1007;
int fa[N], mx[N], mn[N];

int getfa(int x) {
    return x == fa[x] ? x : fa[x] = getfa(fa[x]);
}

void unit(int x, int y) {
    x = getfa(x), y = getfa(y);
    if (x == y) return;
    fa[x] = y;
    mx[y] = max(mx[y], mx[x]);
    mn[y] = min(mn[y], mn[x]);
}

int main() {
    int n, m;
    scanf("%d%d", &n, &m);
    for (int i = 1; i <= n; i++) fa[i] = mx[i] = mn[i] = i;
    while (m--) {
        int l, r;
        scanf("%d%d", &l, &r);
        for (int i = l; i < r; i++)
            unit(i, i + 1);
    }
    int ans = n + 1;
    for (int i = 1; i <= n; i++)
        if (getfa(i) == i) 
            ans += (mx[i] - mn[i]) * 2;
    printf("%d\n", ans);
}