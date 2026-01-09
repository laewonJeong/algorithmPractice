class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0

        for i in range(n-2):
            if nums[i] + nums[i+2] + nums[i] + nums[i+2] == nums[i+1]:
                answer+=1
        
        return answer