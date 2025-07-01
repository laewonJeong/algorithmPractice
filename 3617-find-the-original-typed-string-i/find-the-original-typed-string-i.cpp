class Solution {
public:
    int possibleStringCount(string word) {

        int cnt = 0;
        int temp = 0;
        int answer = 0;
        int n = word.length();
        word += 'A';


        for(int i = 0; i< n; i++){
            if(word[i] == word[i+1]){
                temp += 1;
            }
            else{
                if(temp!=0){
                    temp++;
                    answer += temp - 1;
                    cnt++;
                }
                temp = 0;
            }

        }

        if(answer == 0)
            return 1;
        return answer + 1;
    }
};