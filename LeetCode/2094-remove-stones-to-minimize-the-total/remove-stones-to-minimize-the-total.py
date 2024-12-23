class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles_with_idx = [(-pile, idx) for idx, pile in enumerate(piles)]
        heapq.heapify(piles_with_idx)

        for _ in range(k):
            _, idx = heapq.heappop(piles_with_idx)
            piles[idx] -= piles[idx]//2
            heapq.heappush(piles_with_idx, (-piles[idx], idx))
        
        return sum(piles)

        