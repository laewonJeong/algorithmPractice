class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        dice = [0] * 7
        
        for i in range(n):
            if tops[i] != bottoms[i]:
                dice[bottoms[i]] += 1
            dice[tops[i]] += 1
        
        if max(dice) != n:
            return -1
        
        if dice[tops[0]] == n:
            target = tops[0]
        else:
            target = bottoms[0]

        x = tops.count(target)
        y = bottoms.count(target)
        answer = min(n-x, n-y)

        return answer