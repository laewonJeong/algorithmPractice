class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        answer = 1
        n = len(nums)
        is_len, ds_len = 1, 1

        for i in range(n-1):
            if nums[i] < nums[i+1]:
                is_len += 1
            else:
                is_len = 1
            
            answer = max(answer, is_len)
        
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                ds_len += 1
            else:
                ds_len = 1
            
            answer = max(answer, ds_len)
        
        return answer