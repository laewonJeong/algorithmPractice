class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        nums_counter = Counter(nums)
        left_counter = Counter()

        for i, num in enumerate(nums):
            left_counter[num] += 1
            nums_counter[num] -= 1

            if left_counter[num] * 2 > i + 1 and nums_counter[num] * 2 > n-i-1:
                return i

        return -1
            
            