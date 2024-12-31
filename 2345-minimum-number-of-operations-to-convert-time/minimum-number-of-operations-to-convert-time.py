def change_to_minute(time):
    time = time.split(':')
    return int(time[0]) * 60 + int(time[1])

class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        if current == correct:
            return 0

        current = change_to_minute(current)
        correct = change_to_minute(correct)


        dp = [float('inf') for _ in range(correct - current + 1)]
        minutes = [1, 5, 15, 60]

        for i in range(1, correct-current+1):
            if i in minutes:
                dp[i] = 1
            else:
                for minute in minutes:
                    if i-minute > 0:
                        dp[i] = min(dp[i], dp[i-minute] + dp[minute])

        return dp[-1]
        