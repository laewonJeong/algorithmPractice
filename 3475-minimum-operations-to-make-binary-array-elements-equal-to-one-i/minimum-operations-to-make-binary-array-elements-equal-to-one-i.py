class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0
        
        for i in range(n - 2):
            if nums[i] == 0:
                nums[i] = 1
                nums[i+1] = 0 if nums[i+1] == 1 else 1
                nums[i+2] = 0 if nums[i+2] == 1 else 1
                answer += 1
        
        return answer if all(nums) else -1