class Solution {
public:
    int matchPlayersAndTrainers(vector<int>& players, vector<int>& trainers) {
        sort(players.begin(), players.end(), greater<>());
        sort(trainers.begin(), trainers.end(), greater<>());
        int answer = 0;
        int trainers_idx = 0;
        int n = trainers.size();

        for(auto& player:players){
            if(trainers_idx < n && player <= trainers[trainers_idx]){
                answer++;
                trainers_idx++;
            }
        }
            
        return answer;
    }
};