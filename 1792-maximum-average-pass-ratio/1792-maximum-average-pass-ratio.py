def heapPush(p, t, hq):
    pass_ratio = p/t
    increase_pass_ratio = (p+1)/(t+1)
    heapq.heappush(hq, (-(increase_pass_ratio - pass_ratio),p,t))

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        hq = []

        for p, t in classes:
            heapPush(p,t,hq)
        
        for i in range(extraStudents):
            _, p, t = heapq.heappop(hq)
            heapPush(p+1,t+1,hq)
        
        sum_pass_ratio = 0
        for _, p, t in hq:
            sum_pass_ratio += p/t

        return sum_pass_ratio/len(classes)

        