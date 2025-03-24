from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        merged = []
        
        for start, end in meetings:
            if not merged or merged[-1][1] < start:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)
        
        busy_days = sum(end - start + 1 for start, end in merged)
        
        return days - busy_days
