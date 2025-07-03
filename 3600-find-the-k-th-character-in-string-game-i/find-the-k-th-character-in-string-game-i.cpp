class Solution {
public:
    char kthCharacter(int k) {
        string word = "a";

        while(1){
            string new_word = "";

            for(char ch:word){
                new_word += char(ch+1);
            }
            word += new_word;

            if(word.length() >= k)
                break;

        }

        return word[k-1];
    }
};