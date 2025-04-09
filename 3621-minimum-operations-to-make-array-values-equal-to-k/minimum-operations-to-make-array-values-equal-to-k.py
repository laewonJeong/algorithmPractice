class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        check = False
        nums_set = set()
        for num in nums:
            if num < k:
                return -1
            elif num == k:
                check = True
            nums_set.add(num)
        
        return len(nums_set) if not check else len(nums_set)-1