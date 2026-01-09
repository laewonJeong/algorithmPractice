def backtracking(nums, visited, n, now, arr, j, check):
    for i in range(j,n):
        if visited[i] == 0:
            arr.append(nums[i])
            visited[i] = 1
            backtracking(nums, visited, n, now+1, arr, i, check)
            if now == 0:
                check[arr[0]] += 1
            else:
                or_result = arr[0]
                for k in range(1, now+1):
                    or_result = or_result | arr[k]
                check[or_result] += 1

            visited[i] = 0
            arr.pop()

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        check = defaultdict(int)
        n = len(nums)
        visited = [0] * n

        backtracking(nums, visited, n, 0, [], 0, check)
        
        return check[max(check.keys())]