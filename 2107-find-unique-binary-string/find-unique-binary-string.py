class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        answer = ''
        def backtracking(now, len_now):
            if len_now == n:
                return '' if now in nums else now

            for i in ['0', '1']:
                answer = backtracking(now+i, len_now+1)
                if answer != '':
                    return answer
            
            return answer
        
        return backtracking('',0)