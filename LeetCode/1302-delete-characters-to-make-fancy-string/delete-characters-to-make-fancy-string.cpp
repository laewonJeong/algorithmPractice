class Solution {
public:
    string makeFancyString(string s) {
        string answer;
        answer += s[0];
        int n = s.length();
        char prev_ch = s[0];
        int cnt = 1;

        for(int i = 1;i<n;i++){
            if(prev_ch == s[i])
                cnt++;
            else{
                prev_ch = s[i];
                cnt = 1;
            }

            if(cnt < 3)
                answer += s[i];
        }
        

        return answer;
    }
};