class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()

        if nums[0] + nums[1] <= nums[2]:
            return "none"
        
        nums = set(nums)
        n = len(nums)

        if n == 1:
            return "equilateral"
        elif n == 2:
            return "isosceles"
        else:
            return "scalene"