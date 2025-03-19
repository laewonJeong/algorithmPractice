class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0
        for i in range(2, n):
            if nums[i-2] == 0:
                nums[i-2] = 1
                nums[i-1] = 0 if nums[i-1] == 1 else 1
                nums[i] = 0 if nums[i] == 1 else 1
                answer += 1
        
        if any(num == 0 for num in nums):
            return -1
        else:
            return answer