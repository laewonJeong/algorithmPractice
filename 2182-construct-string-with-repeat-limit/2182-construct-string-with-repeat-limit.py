class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count_s = Counter(s)
        hq = [(-ord(k), v) for k,v in count_s.items()]
        heapq.heapify(hq)

        answer = ""

        while hq:
            current_alpha, cnt = heapq.heappop(hq)
            answer += chr(-current_alpha) * min(repeatLimit, cnt)

            if cnt > repeatLimit and hq:
                next_alpha, next_cnt = heapq.heappop(hq)
                answer += chr(-next_alpha)
                if next_cnt > 1:
                    heapq.heappush(hq, (next_alpha, next_cnt - 1))
                heapq.heappush(hq, (current_alpha, cnt-repeatLimit))

        return answer