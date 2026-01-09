class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd_cnt = 0
        for num in arr:
            if num % 2 == 0:
                odd_cnt = 0
            else:
                odd_cnt += 1
                if odd_cnt == 3:
                    return True
        
        return False

