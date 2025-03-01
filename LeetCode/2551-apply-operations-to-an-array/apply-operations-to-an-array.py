class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = []

        for i in range(n):
            if i+1 < n and nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
            
            if nums[i] != 0:
                answer.append(nums[i])
        
        for _ in range(n-len(answer)):
            answer.append(0)

        return answer