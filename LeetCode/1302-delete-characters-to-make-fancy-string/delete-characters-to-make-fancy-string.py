class Solution:
    def makeFancyString(self, s: str) -> str:
        n = len(s)
        answer = s[0]
        prev_ch = s[0]
        cnt = 1

        for i in range(1,n):
            if s[i] == prev_ch:
                cnt+=1
            else:
                prev_ch = s[i]
                cnt = 1
            
            if cnt < 3:
                answer += s[i]
        
        return answer

