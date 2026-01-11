class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict = defaultdict(int)
        for num in nums:
            dict[num] += 1

        for k, v in dict.items():
            if v == 1:
                return k