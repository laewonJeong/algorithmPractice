class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        def build_lps(pattern: str) -> List[int]:
            m = len(pattern)
            lps = [0] * m
            j = 0
            for i in range(1, m):
                while j > 0 and pattern[i] != pattern[j]:
                    j = lps[j - 1]
                if pattern[i] == pattern[j]:
                    j += 1
                    lps[i] = j
            return lps

        def kmp_search(text: str, pattern: str) -> bool:
            n, m = len(text), len(pattern)
            lps = build_lps(pattern)
            j = 0
            for i in range(n):
                while j > 0 and text[i] != pattern[j]:
                    j = lps[j - 1]
                if text[i] == pattern[j]:
                    j += 1
                if j == m:
                    return True
            return False

        n = len(words)
        answer = []
        for i in range(n):
            for j in range(n):
                if i != j and kmp_search(words[j], words[i]):
                    answer.append(words[i])
                    break
        
        return answer
