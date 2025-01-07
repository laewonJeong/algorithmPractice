class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        answer = set()

        for i in range(n):
            for j in range(n):
                if words[i] != words[j] and words[i] in words[j]:
                    answer.add(words[i])
        
        return list(answer)