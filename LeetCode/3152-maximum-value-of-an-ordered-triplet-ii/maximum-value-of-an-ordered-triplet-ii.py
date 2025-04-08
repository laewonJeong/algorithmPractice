class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        answer = 0
        minus_op = 0
        first_num = 0

        for num in nums:
            answer = max(answer, minus_op * num)
            minus_op = max(minus_op, first_num - num)
            first_num = max(first_num, num)
    
        return answer