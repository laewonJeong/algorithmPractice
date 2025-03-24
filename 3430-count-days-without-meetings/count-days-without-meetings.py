class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        n = len(meetings)
        meetings.sort(key = lambda x:(x[0], -x[1]))
        before = -1
        before_idx = 0

        for i in range(n):
            if meetings[i][0] != before and meetings[i][0] <= meetings[before_idx][1]:
                meetings[i][0] = meetings[before_idx][0]
                meetings[i][1] = max(meetings[i][1], meetings[before_idx][1])
                before = meetings[i][0]
                before_idx = i
            elif meetings[i][0] == before:
                meetings[i][0] = meetings[before_idx][0]
                meetings[i][1] = max(meetings[i][1], meetings[before_idx][1])
            else:
                before = meetings[i][0]
                before_idx = i
            
            if i != 0 and meetings[i-1][0] != meetings[i][0]:
                days -= (meetings[i-1][1] - meetings[i-1][0] + 1)
    
        return days -(meetings[-1][1] - meetings[-1][0] + 1)