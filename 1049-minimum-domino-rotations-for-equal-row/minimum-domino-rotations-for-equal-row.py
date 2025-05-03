class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        dice = [0] * 7
        
        for i in range(n):
            if tops[i] == bottoms[i]:
                dice[tops[i]] += 1
            else:
                dice[tops[i]] += 1
                dice[bottoms[i]] += 1
        
        if max(dice) != n:
            return -1
        
        answer = 0
        for i in range(1, 7):
            if dice[i] == n:
                x = tops.count(i)
                y = bottoms.count(i)
                answer = min(n-x, n-y)

        return answer