class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        
        vowel = False
        consonant = False

        for ch in word:
            if ch.isdigit():
                continue
            elif ch in ['@','#','$']:
                return False
            elif ch in 'aeiouAEIOU':
                vowel = True
            else:
                consonant = True
        
        return vowel and consonant


        
        return True