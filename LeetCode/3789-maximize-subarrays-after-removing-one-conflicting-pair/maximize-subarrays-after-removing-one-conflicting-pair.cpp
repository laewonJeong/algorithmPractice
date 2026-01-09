class Solution {
public:
    long long maxSubarrays(int n, vector<vector<int>>& conflictingPairs) {
        vector<int> bMin1(n + 1, n + 1), bMin2(n + 1, n + 1);
        for (const auto& pair : conflictingPairs) {
            int a = min(pair[0], pair[1]), b = max(pair[0], pair[1]);
            if (bMin1[a] > b) {
                bMin2[a] = bMin1[a];
                bMin1[a] = b;
            } else if (bMin2[a] > b) {
                bMin2[a] = b;
            }
        }
        long long res = 0;
        int b1 = n + 1, b2 = n + 1;
        vector<long long> delCount(n + 2, 0);
        for (int i = n; i >= 1; i--) {
            if (b1 > bMin1[i]) {
                b2 = min(b1, bMin2[i]);
                b1 = bMin1[i];
            } else {
                b2 = min(b2, bMin1[i]);
            }
            res += b1 - i;
            delCount[b1] += b2 - b1;
        }
        return res + *max_element(delCount.begin(), delCount.end());
    }
};