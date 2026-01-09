class Solution {
public:
    int findLucky(vector<int>& arr) {
        vector<int> cnt(*max_element(arr.begin(), arr.end()) + 1);
        int answer = -1;

        for(int num:arr){
            cnt[num]++;
        }

        for(int i = 1; i < cnt.size(); i++){
            if(i == cnt[i])
                answer = i;
        }   

        return answer;
    }
};