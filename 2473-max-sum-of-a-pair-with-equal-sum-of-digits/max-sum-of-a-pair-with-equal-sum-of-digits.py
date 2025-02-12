class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        count = defaultdict(list)
        answer = -1

        def get_sum_digit(num):
            sum_digit = 0

            while num != 0:
                sum_digit += num % 10
                num //= 10
            
            return sum_digit

        for num in nums:
            sum_digit = get_sum_digit(num)
            if len(count[sum_digit]) == 2 and num < -count[sum_digit][0] and num < -count[sum_digit][1]:
                continue
            heapq.heappush(count[sum_digit], -num)
        
        for k, v in count.items():
            if len(count[k]) > 1:
                i = heapq.heappop(count[k])
                j = heapq.heappop(count[k])

                answer = max(answer, -i-j)
        
        return answer