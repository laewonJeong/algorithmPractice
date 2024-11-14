def binary_search(nums, n, start, is_left):
    left, right = start, len(nums)

    while left < right:
        mid = (left+right)//2

        if nums[mid] < n and is_left:
            left = mid+1
        elif nums[mid] <= n and not is_left:
            left = mid+1
        else:
            right = mid

    return left

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        answer = 0

        for i in range(n):
            left = binary_search(nums, lower-nums[i], i+1, True)
            right = binary_search(nums, upper-nums[i], i+1, False)
            answer += right - left
            
        return answer