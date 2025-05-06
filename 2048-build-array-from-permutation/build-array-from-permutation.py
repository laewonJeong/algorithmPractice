class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = []

        for i in range(n):
            answer.append(nums[nums[i]])
        
        return answer
