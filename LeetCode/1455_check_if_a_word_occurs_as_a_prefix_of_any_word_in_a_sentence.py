class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        n = len(searchWord)

        for i, word in enumerate(words):
            word_prefix = word[:n]
            if word_prefix == searchWord:
                return i+1

        return -1 
