class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        answer = 0
        zero = 0

        for num in nums:
            if num == 0:
                zero+=1
                answer+=zero
            else:
                zero = 0
            
        return answer