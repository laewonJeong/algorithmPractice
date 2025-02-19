class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        cnt = 0
        answer = ''
        def backtracking(n, k, now, s):
            nonlocal cnt
            nonlocal answer

            if answer != '':
                return

            if now == n:
                cnt += 1
                if cnt == k:
                    answer = s
                return

            for i in ['a', 'b', 'c']:
                if not s or s[-1] != i:
                    backtracking(n, k, now+1, s + i)
        
        backtracking(n,k,0,'')
        return answer
