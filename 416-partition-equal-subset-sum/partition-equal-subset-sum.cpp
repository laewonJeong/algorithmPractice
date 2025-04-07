class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum_num = accumulate(nums.begin(), nums.end(), 0);

        if (sum_num % 2 != 0){
            return false;
        }

        int div_sum_num = sum_num / 2;
        vector<bool> dp(div_sum_num+1, false);
        dp[0] = true;

        for (int num:nums){
            for(int i = div_sum_num; i >= num; --i){
                dp[i] = dp[i] || dp[i-num];
            }
        }
        
        return dp[div_sum_num];
    }
};