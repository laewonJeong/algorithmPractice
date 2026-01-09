class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        
        if 0 not in nums:
            return n - 1
        
        right = 0
        zero_count = 0
        answer = 0

        for left in range(n):
            while right < n and zero_count <= 1:
                if nums[right] == 0:
                    zero_count += 1
                if zero_count == 1:
                    answer = max(answer, right-left)
                right+=1

            if nums[left] == 0:
                zero_count -= 1
            
            

        return answer