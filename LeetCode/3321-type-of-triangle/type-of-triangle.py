class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = nums
        if a + b <= c or a + c <= b or c + b <= a:
            return "none"
        
        nums = set(nums)
        n = len(nums)

        if n == 1:
            return "equilateral"
        elif n == 2:
            return "isosceles"
        else:
            return "scalene"