class Solution {
public:
    int maximumGain(string s, int x, int y) {
        vector<char> stack;
        int answer = 0;
        char sub1 = 'a';
        char sub2 = 'b';
        if(y > x){
            sub1 = 'b';
            sub2 = 'a';
            swap(x, y);
        }

        for(auto ch:s){
            if(!stack.empty() && stack.back() == sub1 && ch == sub2){
                answer += x;
                stack.pop_back();
            }
            else
                stack.push_back(ch);
        }

        vector<char> new_stack;
        
        for(auto ch:stack){
            if(!new_stack.empty() && new_stack.back() == sub2 && ch == sub1){
                answer += y;
                new_stack.pop_back();
            }
            else
                new_stack.push_back(ch);
        }

        return answer;
    }
};