class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        left, right = min(nums), max(nums)
        n = len(nums)
        
        while left < right:
            mid = (left+right)//2
            cnt = 0
            i = 0
            while i < n:
                if nums[i] <= mid:
                    i += 1
                    cnt += 1
                i += 1

            if cnt < k:
                left = mid + 1
            else:
                right = mid
        
        return left