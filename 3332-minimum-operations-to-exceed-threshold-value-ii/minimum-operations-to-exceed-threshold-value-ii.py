class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        answer = 0

        while True:
            x = heapq.heappop(nums)
            if x >= k:
                break
            y = heapq.heappop(nums)
            heapq.heappush(nums, x * 2 + y)
            answer += 1
            
        return answer