class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0 for _ in range(days[-1]+1)]
        
        day_check = defaultdict(bool)
        for day in days:
            day_check[day] = True
        

        for i in range(1, days[-1]+1):
            if not day_check[i]:
                dp[i] = dp[i-1]
            else:
                if i-7 < 0:
                    dp[i] = min(dp[i-1] + costs[0], costs[1], costs[2])
                elif i-30 < 0:
                    dp[i] = min(dp[i-1] + costs[0], dp[i-7] + costs[1], costs[2])
                else:
                    dp[i] = min(dp[i-1] + costs[0], dp[i-7] + costs[1], dp[i-30] + costs[2])

        return dp[-1]