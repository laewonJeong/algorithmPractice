class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        num = ''.join([str(n) for n in nums])
        return [int(n) for n in num]
