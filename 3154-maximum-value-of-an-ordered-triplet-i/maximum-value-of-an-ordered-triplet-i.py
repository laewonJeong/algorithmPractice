class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        minus_op = 0
        first_num = 0
        answer = 0

        for i in range(n):
            answer = max(answer, minus_op * nums[i])
            minus_op = max(minus_op, first_num - nums[i])
            first_num = max(first_num, nums[i])
        
        return answer