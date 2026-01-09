class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        answer = 0

        for i, num in enumerate(nums):
            left = max(bisect_left(nums, lower - num), i+1)
            right = max(bisect_right(nums, upper - num), i+1)
            answer += right - left
        
        return answer