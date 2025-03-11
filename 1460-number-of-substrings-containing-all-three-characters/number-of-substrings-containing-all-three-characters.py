class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        abc = {'a':0, 'b':0, 'c':0}
        n = len(s)
        left = 0
        answer = 0
        cnt = 0

        for right in range(n):
            abc[s[right]] += 1
            if abc[s[right]] == 1:
                cnt += 1
            
            if cnt == 3:
                while True:
                    answer += n - right
                    abc[s[left]] -= 1
                    if abc[s[left]] == 0:
                        left+=1
                        break
                    left += 1
                cnt -= 1

        return answer