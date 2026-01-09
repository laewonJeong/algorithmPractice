class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        d_length = 0
        answer = 0

        for d in dimensions:
            if d_length < sqrt(d[0] ** 2 + d[1] ** 2):
                d_length = sqrt(d[0] ** 2 + d[1] ** 2)
                answer = d[0] * d[1]
            elif d_length == sqrt(d[0] ** 2 + d[1] ** 2):
                answer = max(answer, d[0] * d[1])

        return answer