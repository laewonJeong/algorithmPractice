class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        answer = 0
        max_num = max(nums)

        l = 0
        for num in nums:
            if num == max_num:
                l+=1
            else:
                answer = max(l, answer)
                l = 0
        
        return max(l, answer)