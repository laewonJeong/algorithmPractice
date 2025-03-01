class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = []
        zero = []

        for i in range(n):
            if i+1 < n and nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
            
            if nums[i] != 0:
                answer.append(nums[i])
            else:
                zero.append(0)
     

        return answer+zero