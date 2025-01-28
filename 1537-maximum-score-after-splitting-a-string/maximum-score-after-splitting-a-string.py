class Solution:
    def maxScore(self, s: str) -> int:
        answer = 0

        dic_left = {'0':0, '1':0}
        dic_right = {'0':0, '1':0}
        
        for num in s:
            dic_right[num] += 1
        
        for i in range(len(s)-1):
            dic_right[s[i]] -= 1
            dic_left[s[i]] += 1
            answer = max(answer, dic_right['1'] + dic_left['0'])

        
        return answer