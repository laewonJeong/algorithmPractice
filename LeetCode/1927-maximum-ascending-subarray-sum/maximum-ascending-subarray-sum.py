class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        answer = nums[0]
        n = len(nums)
        sum_sub_array = nums[0]

        for i in range(1, n):
            if nums[i-1] < nums[i]:
                sum_sub_array += nums[i]
            else:
                sum_sub_array = nums[i]
            answer = max(answer, sum_sub_array)
        
        return answer