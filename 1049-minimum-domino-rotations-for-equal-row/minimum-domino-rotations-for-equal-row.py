class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        dice = [0] * 6
        
        for i in range(n):
            if tops[i] == bottoms[i]:
                dice[tops[i] - 1] += 1
            else:
                dice[tops[i] - 1] += 1
                dice[bottoms[i] - 1] += 1
        
        if max(dice) != n:
            return -1
        
        answer = 0
        for i in range(6):
            if dice[i] == n:
                x = tops.count(i+1)
                y = bottoms.count(i+1)
                answer = max(0, min(n-x, n-y))

        return answer