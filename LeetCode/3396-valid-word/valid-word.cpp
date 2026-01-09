bool isVowel(char ch){
    ch = tolower(ch);
    if(ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' ||ch == 'u')
        return true;
    
    return false;
}

class Solution {
public:
    bool isValid(string word) {
        if(word.length() < 3)
            return false;

        bool vowel = false;
        bool consonant = false;

        for(auto ch: word){
            if(isdigit(ch))
                continue;
            else if(ch == '@' || ch == '#' || ch == '$')
                return false;
            else if(isVowel(ch))
                vowel = true;
            else
                consonant = true;
        }

        return vowel && consonant;
    }
};