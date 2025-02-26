class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer = nums[0]
        now_sum = 0

        for num in nums:
            if now_sum < 0:
                now_sum = 0
            
            now_sum += num

            answer = max(answer, now_sum)

        return answer