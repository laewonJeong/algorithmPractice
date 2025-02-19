class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        cnt = 0

        def backtracking(now, s):
            nonlocal cnt

            if now == n:
                cnt += 1
                return s if cnt == k else ""

            for i in ['a', 'b', 'c']:
                if not s or s[-1] != i:
                    answer = backtracking(now+1, s + i)
                    if answer:
                        return answer
            
            return answer
        
        return backtracking(0,'')
