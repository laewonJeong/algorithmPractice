class Solution(object):
    def maxFreeTime(self, eventTime, k, startTime, endTime):
        n = len(startTime)
        meeting_time = 0
        for st, et in zip(startTime, endTime):
            meeting_time += et-st
        
        if n == k:
            return eventTime - meeting_time
        

        free_time = [startTime[0] - 0]
        for i in range(1,n):
            free_time.append(startTime[i] - endTime[i-1])
        free_time.append(eventTime - endTime[-1])

        answer = sum(free_time[:k+1])
        max_free_time = answer

        for i in range(k+1, n+1):
            max_free_time += free_time[i] - free_time[i-k-1]
            answer = max(answer, max_free_time)

        return answer