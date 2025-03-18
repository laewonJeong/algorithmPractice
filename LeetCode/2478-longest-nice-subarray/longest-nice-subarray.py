class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        answer = 1

        for right in range(len(nums)):
            now = nums[right]
            left = right -1
            while left >= 0 and now & nums[left] == 0:
                now |= nums[left]
                left -= 1
            
            answer = max(answer, right - left)

        return answer