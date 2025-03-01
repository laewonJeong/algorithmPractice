class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        
        for i in range(n):
            if nums[i] == 0:
                for j in range(i+1, n):
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break

        return nums