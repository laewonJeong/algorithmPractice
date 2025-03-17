class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums_count = Counter(nums)
        return all(cnt % 2 == 0 for cnt in nums_count.values())