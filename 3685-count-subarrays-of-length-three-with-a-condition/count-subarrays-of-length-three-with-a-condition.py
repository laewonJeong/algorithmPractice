class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0

        for i in range(n-2):
            s = nums[i:i+3]
            if s[0] + s[2] == s[1]/2:
                answer+=1
        
        return answer