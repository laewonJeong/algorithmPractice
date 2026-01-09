class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        answer = 0
        subseq = ""

        for i in range(n - 1, -1, -1):
            temp = s[i] + subseq

            if int(temp, 2) <= k:
                subseq = temp
                answer += 1

        return answer
