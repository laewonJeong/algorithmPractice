class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        q = deque(sorted(queries))
        available = []
        working = []

        for i in range(n):
            while q and q[0][0] <= i:
                heapq.heappush(available, -q.popleft()[1])

            while working and working[0] < i:
                heapq.heappop(working)

            while nums[i] > len(working):
                if available and -available[0] >= i:
                    heapq.heappush(working, -heapq.heappop(available))
                else:
                    return -1

        return len(available)