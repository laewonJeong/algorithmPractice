class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        sum_result = 0
        answer = 0

        for right in range(n):
            sum_result += nums[right]
            while left <= right and sum_result * (right - left + 1) >= k:
                sum_result -= nums[left]
                left += 1

            answer += right - left + 1

        return answer