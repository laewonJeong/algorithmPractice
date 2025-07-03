class Solution {
public:
    char kthCharacter(int k) {
        string word = "a";
        int word_len = 1;

        while(1){
            string new_word = "";

            for(char ch:word){
                new_word += char(ch+1);
            }
            word += new_word;
            word_len *= 2;

            if(word_len >= k)
                break;

        }

        return word[k-1];
    }
};