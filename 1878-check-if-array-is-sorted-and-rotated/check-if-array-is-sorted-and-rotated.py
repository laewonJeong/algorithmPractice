class Solution:
    def check(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        n = len(nums)

        for i in range(n):
            check = 0
            for j in range(n):
                if nums[(j+i) % n] == sorted_nums[j]:
                    check += 1
                
            if check == n:
                return True
        
        return False
                    