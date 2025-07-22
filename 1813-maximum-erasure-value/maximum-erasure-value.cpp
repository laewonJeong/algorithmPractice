class Solution {
public:
    int maximumUniqueSubarray(vector<int>& nums) {
        vector<bool> unique(10001, false);
        int sub_sum = 0;
        int answer = 0;

        auto left = nums.begin();
        auto right = nums.begin();

        while (left != nums.end()) {
            while (right != nums.end() && !unique[*right]) {
                sub_sum += *right;
                unique[*right] = true;
                ++right;
            }

            answer = max(answer, sub_sum);
            unique[*left] = false;
            sub_sum -= *left;
            ++left;
        }

        return answer;
    }
};
