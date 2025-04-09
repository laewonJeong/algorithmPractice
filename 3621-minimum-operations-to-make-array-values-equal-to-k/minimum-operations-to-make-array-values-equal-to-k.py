class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums) < k:
            return -1
        
        answer = 0
        seen = set()
        for num in nums:
            if num == k:
                continue
            elif num not in seen:
                answer += 1
                seen.add(num)
        
        return answer