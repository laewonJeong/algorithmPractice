class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        idx = 0
        answer = 0

        dic = defaultdict(int)
        for i in range(len(s)):
            dic[s[i]] += 1
            if dic[s[i]] > 2:
                while dic[s[i]] > 2:
                    dic[s[idx]] -= 1
                    idx+=1
            answer = max(answer, i - idx + 1)

        return answer