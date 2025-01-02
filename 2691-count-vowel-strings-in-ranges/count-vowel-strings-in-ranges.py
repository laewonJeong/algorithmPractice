class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        prefix = [0 for _ in range(n)]
        vowels = ['a', 'e', 'i', 'o', 'u']
        answer = []

        if words[0][0] in vowels and words[0][-1] in vowels:
            prefix[0] = 1

        for i in range(1, n):
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefix[i] = prefix[i-1] + 1
            else:
                prefix[i] = prefix[i-1]

        for query in queries:
            if query[0] == 0:
                answer.append(prefix[query[1]])
            else:
                answer.append(prefix[query[1]] - prefix[query[0]-1])
        
        return answer