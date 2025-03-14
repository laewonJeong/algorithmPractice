class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        def find_zero(nums, queries, mid):
            n = len(nums)
            different_list = [0] * (n+1)
            total_sum = 0
            for i in range(mid):
                l, r, val = queries[i]
                different_list[l] += val
                different_list[r+1] -= val

            for num_index in range(n):
                total_sum += different_list[num_index]
                if total_sum < nums[num_index]:
                    return False
            return True
        
        left, right = 0, len(queries)

        if not find_zero(nums, queries, right):
            return -1

        while left <= right:
            mid = left + (right - left) // 2

            if find_zero(nums, queries, mid):
                right = mid - 1
            else:
                left = mid + 1

        return left