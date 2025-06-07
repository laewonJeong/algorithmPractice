class Solution:
    def clearStars(self, s: str) -> str:
        s = list(s)
        n = len(s)
        hq = []

        for i in range(n):
            if s[i] == '*':
                _, j = heapq.heappop(hq)
                s[-j] = ''
                s[i] = ''
            else:
                heapq.heappush(hq, (s[i], -i))
        
        return ''.join(s)