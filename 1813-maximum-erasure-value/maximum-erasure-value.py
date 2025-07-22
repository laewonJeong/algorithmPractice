class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        answer = sub_sum = left = 0

        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                sub_sum -= nums[left]
                left += 1
            seen.add(nums[right])
            sub_sum += nums[right]
            answer = max(answer, sub_sum)

        return answer