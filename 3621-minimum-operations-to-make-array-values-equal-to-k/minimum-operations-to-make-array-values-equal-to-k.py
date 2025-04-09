class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums) < k:
            return -1
        
        nums = set(nums)
        answer = 0
        for num in nums:
            if num > k:
                answer += 1
        
        return answer