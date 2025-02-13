class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        answer = 0

        while True:
            min_num = heapq.heappop(nums)
            if min_num < k:
                max_num = heapq.heappop(nums)
                heapq.heappush(nums, min_num * 2 + max_num)
                answer += 1
            else:
                break
        
        return answer