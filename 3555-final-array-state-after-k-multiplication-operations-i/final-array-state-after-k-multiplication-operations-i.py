class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        hq = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(hq)

        for _ in range(k):
            num, idx = heapq.heappop(hq)
            heapq.heappush(hq, (num*multiplier, idx))
            nums[idx] *= multiplier
        
        return nums