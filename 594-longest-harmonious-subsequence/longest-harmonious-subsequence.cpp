class Solution {
public:
    int findLHS(vector<int>& nums) {
        unordered_map<int, int> cnt;

        for (int num:nums){
            cnt[num]++;
        }

        int answer = 0;

        for(auto& [key, value]:cnt ){
            if(cnt.count(key+1)){
                answer = max(answer, value + cnt[key+1]);
            }
        }

        return answer;
    }
};