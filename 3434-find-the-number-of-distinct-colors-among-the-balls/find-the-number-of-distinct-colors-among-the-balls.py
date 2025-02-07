class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors = defaultdict(int)
        check_color = Counter()
        answer = []

        cnt = 0
        for query in queries:
            ball, color = query

            if colors[ball] != 0:
                check_color[colors[ball]] -= 1
                if check_color[colors[ball]] == 0:
                    cnt -= 1
                    del check_color[colors[ball]]

            check_color[color] += 1
            colors[ball] = color
            if check_color[color] == 1:
                cnt += 1
            
            answer.append(cnt)

        return answer