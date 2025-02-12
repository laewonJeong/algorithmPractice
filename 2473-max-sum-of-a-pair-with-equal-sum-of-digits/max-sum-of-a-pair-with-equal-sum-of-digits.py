class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        count = defaultdict(list)
        answer = -1

        for num in nums:
            sum_digit = sum(list(map(int, str(num))))
            heapq.heappush(count[sum_digit], -num)
        
        
        for k, v in count.items():
            if len(count[k]) > 1:
                i = heapq.heappop(count[k])
                j = heapq.heappop(count[k])

                answer = max(answer, -i-j)
        
        return answer