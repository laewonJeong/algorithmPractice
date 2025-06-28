class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        nums = [(i, nums[i]) for i in range(len(nums))]

        nums.sort(key = lambda x:-x[1])
        nums = nums[:k]

        nums.sort()

        return [num for _, num in nums]
