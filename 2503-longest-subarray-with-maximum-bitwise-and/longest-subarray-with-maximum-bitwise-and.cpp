class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int max_num = *max_element(nums.begin(), nums.end());
        int answer = 0;
        int l = 0;

        for(auto num:nums){
            if(num == max_num) l++;
            else{
                answer = max(answer, l);
                l = 0;
            }
        }

        return max(answer, l);
    }
};