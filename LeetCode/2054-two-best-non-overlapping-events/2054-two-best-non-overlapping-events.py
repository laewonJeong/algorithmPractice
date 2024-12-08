class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        answer = 0
        n = len(events)
        events.sort()

        max_value = [0] * n
        max_value[-1] = events[-1][2]

        for i in range(n-2, -1, -1):
            max_value[i] = max(max_value[i+1], events[i][2])

        for i, event in enumerate(events):
            answer = max(answer, event[2])
            left, right = 0, n-1
            idx = -1
            while left <= right:
                mid = (left + right) // 2

                if events[mid][0] > event[1]:
                    idx = mid
                    right = mid - 1
                else:
                    left = mid + 1

            if idx != -1:
                answer = max(answer, event[2] + max_value[idx])

        return answer