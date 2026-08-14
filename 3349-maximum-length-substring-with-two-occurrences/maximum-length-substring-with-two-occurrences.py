class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        idx = 0
        dic = defaultdict(int)
        dic[s[idx]] = 1
        answer = 0

        for i in range(1, n):
            dic[s[i]] += 1
            if dic[s[i]] > 2:
                while dic[s[i]] > 2:
                    dic[s[idx]] -= 1
                    idx+=1
            answer = max(answer, i - idx + 1)

        return answer