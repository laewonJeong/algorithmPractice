class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        nums = [[i, num] for i, num in enumerate(nums)]

        nums.sort(key = lambda x:-x[1])
        nums = nums[:k]

        nums.sort()

        return [num for _, num in nums]
