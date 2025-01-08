class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        answer = 0

        for i in range(n):
            for j in range(i+1, n):
                if words[j].find(words[i]) == 0 and words[j].rfind(words[i]) == len(words[j])-len(words[i]):
                    answer += 1
        
        return answer