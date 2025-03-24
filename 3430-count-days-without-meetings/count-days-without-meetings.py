class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        n = len(meetings)
        meetings.sort(key = lambda x:(x[0], -x[1]))
        before = -1
        before_idx = 0
        #print(meetings)
        new_meetings = set()
        for i in range(n):
            if meetings[i][0] != before and meetings[i][0] <= meetings[before_idx][1]:
                meetings[i] = [meetings[before_idx][0], max(meetings[i][1], meetings[before_idx][1])]
                before = meetings[i][0]
                before_idx = i
                new_meetings.add(tuple(meetings[i]))
            elif meetings[i][0] == before:
                meetings[i] = [meetings[before_idx][0], max(meetings[i][1], meetings[before_idx][1])]
            else:
                before = meetings[i][0]
                before_idx = i
                new_meetings.add(tuple(meetings[i]))
        
       # print(meetings)
        new_meetings = list(new_meetings)
        new_meetings.sort(key = lambda x:(x[0], -x[1]))
        before = -1

        for start, end in new_meetings:
            if start != before:
                days -= (end - start + 1)
                before = start
    
        return days