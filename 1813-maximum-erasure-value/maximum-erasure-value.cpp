class Solution {
public:
    int maximumUniqueSubarray(vector<int>& nums) {
        unordered_map<int, bool> unique;
        int n = nums.size();
        int sub_sum = 0;
        int right = 0;
        int answer = 0;

        for(int left = 0; left< n; left++){
            while(right < n && !unique[nums[right]]){
                sub_sum += nums[right];
                unique[nums[right]] = true;
                right++;
            }

            answer = max(answer, sub_sum);
            unique[nums[left]] = false;
            sub_sum -= nums[left];
        }

        return answer;
    }
};