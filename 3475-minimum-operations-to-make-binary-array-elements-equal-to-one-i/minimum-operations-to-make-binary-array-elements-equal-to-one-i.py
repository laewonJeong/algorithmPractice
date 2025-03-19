class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0
        for i in range(2, n):
            if nums[i-2] == 0:
                nums[i-2] = 1
                nums[i-1] ^= 1
                nums[i] ^= 1
                answer += 1
        
        if all(num == 1 for num in nums):
            return answer
        else:
            return -1