class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        left, right = 0, n - 1
        answer = 0

        while left <= right:
            if nums[left] + nums[right] <= target:
                answer += (2 ** (right - left)) 
                answer = answer % (10**9 + 7)
                left += 1
            else:
                right -= 1

        return answer
