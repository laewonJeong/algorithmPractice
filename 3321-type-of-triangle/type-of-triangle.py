class Solution:
    def triangleType(self, nums: List[int]) -> str:
        counter_nums = Counter(nums)
        n = len(counter_nums)

        if n == 1:
            return "equilateral"
        elif n == 2:
            target = -1
            two_side = -1

            for key in counter_nums:
                if counter_nums[key] == 1:
                    target = key
                else:
                    two_side = key
            
            if two_side * 2 > target:
                return "isosceles"
            else:
                return "none"
        else:
            x = nums[0] + nums[1]
            y = nums[0] + nums[2]
            z = nums[1] + nums[2]

            if x > nums[2] and y > nums[1] and z > nums[0]:
                return "scalene"
            else:
                return "none"