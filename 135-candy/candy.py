class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        result = [1] * n
        answer = 0

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                result[i] = result[i-1] + 1
        
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1] and result[i] <= result[i+1]:
                result[i] = result[i+1] + 1
            answer += result[i]
        
        return answer + result[-1]

        