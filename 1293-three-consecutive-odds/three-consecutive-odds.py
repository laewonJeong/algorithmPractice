class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd_cnt = 0
        for num in arr:
            if odd_cnt == 3:
                return True

            if num % 2 == 0:
                odd_cnt = 0
            else:
                odd_cnt += 1
        
        return False if odd_cnt < 3 else True

