class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        for i in range(1, len(meetings)):
            current_start, current_end = meetings[i]
            prev_start, prev_end = meetings[i-1]

            if current_start <= prev_end:
                meetings[i][0] = prev_start
                meetings[i][1] = max(current_end, prev_end)
            
            if prev_start != meetings[i][0]:
                days -= (prev_end - prev_start + 1)
    
        return days - (meetings[-1][1] - meetings[-1][0] + 1)
