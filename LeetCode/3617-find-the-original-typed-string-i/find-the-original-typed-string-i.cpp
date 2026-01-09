class Solution {
public:
    int possibleStringCount(string word) {
        int answer = 0;
        int n = word.length();

        for(int i = 0; i< n; i++){
            if(word[i] == word[i+1]){
                answer++;
            }
        }

        return ++answer;
    }
};