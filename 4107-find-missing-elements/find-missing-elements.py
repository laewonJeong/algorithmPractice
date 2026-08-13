class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        answer = []

        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] != 1:
                for j in range(nums[i - 1] + 1, nums[i]):
                    answer.append(j)
        
        return answer
