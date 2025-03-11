class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        abc = {'a':0, 'b':0, 'c':0}
        n = len(s)
        left = 0
        answer = 0

        for right in range(n):
            abc[s[right]] += 1

            while 0 not in abc.values():
                answer += n - right
                abc[s[left]] -= 1
                left += 1

        return answer