class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        answer = 0

        cnt = 1
        for i in range(-k+1, n-1):
            if colors[i] == colors[i-1]:
                cnt = 1
            else:
                cnt += 1
            
            if cnt == k:
                answer += 1
                cnt -= 1

            
        return answer