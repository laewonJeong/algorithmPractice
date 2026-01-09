class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)

        left = 0
        result = 0
        pairs = 0
        length = len(nums)

        for right in range(length):
            num = nums[right]
            pairs += counts[num]
            counts[num] += 1

            while pairs >= k:
                 result += length - right
                 counts[nums[left]] -= 1
                 pairs -= counts[nums[left]]
                 left += 1

        return result