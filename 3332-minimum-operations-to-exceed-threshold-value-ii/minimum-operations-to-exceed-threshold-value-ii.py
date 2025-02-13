class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        answer = 0

        while True:
            x = heapq.heappop(nums)
            if x >= k:
                break
            heapq.heapreplace(nums, x * 2 + nums[0])
            answer += 1
            
        return answer