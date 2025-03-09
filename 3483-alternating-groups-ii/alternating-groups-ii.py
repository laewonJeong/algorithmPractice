class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors += colors[:k]
        n = len(colors)

        answer = 0
        l,r = 0,1

        answer = 0
        while r < n:
            if r-l == k:
                answer += 1
                l+=1
            elif colors[r] == colors[r-1]:
                l = r
                r +=1
                continue
            else:
                r+=1
                continue
        return answer