class Solution {
public:
    int findLHS(vector<int>& nums) {
        unordered_map<int, int> cnt;

        for (int num:nums){
            cnt[num]++;
        }

        int answer = 0;

        for(int num:nums){
            if(cnt.count(num+1)){
                answer = max(answer, cnt[num] + cnt[num+1]);
            }
        }

        return answer;
    }
};