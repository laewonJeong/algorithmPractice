class Solution(object):
    def pickGifts(self, gifts, k):
        gifts = [-gift for gift in gifts]
        heapq.heapify(gifts)

        for _ in range(k):
            max_gift = heapq.heappop(gifts)
            heapq.heappush(gifts, -floor(sqrt(-max_gift)))
        
        return int(-sum(gifts))
        
        