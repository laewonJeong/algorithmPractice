class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0
        visited = [0] * n
        check = set()
        
        def backtracking(now, xor_value, nums, visited, temp):
            nonlocal answer
            
            check_tup = tuple(sorted(temp))
            if check_tup in check:
                return
            else:
                answer += xor_value
                check.add(check_tup)
            
            if now == n:
                return
            
            for i in range(n):
                if not visited[i]:
                    visited[i] = 1
                    backtracking(now+1, xor_value ^ nums[i], nums, visited, temp + [i])
                    visited[i] = 0

        backtracking(0, 0, nums, visited, [])

        return answer