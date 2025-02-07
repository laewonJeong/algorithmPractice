class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = {}
        check_color = Counter()
        answer = []

        cnt = 0
        for query in queries:
            ball, color = query

            if ball in balls:
                check_color[balls[ball]] -= 1
                if check_color[balls[ball]] == 0:
                    del check_color[balls[ball]]

            check_color[color] += 1
            balls[ball] = color

            answer.append(len(check_color))

        return answer