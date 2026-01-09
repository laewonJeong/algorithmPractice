class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dic = defaultdict(int)

        for domino in dominoes:
            if domino[0] > domino[1]:
                domino = [domino[1], domino[0]]
            dic[tuple(domino)] += 1
        
        answer = 0

        for key in dic:
            cnt = dic[key]
            if cnt > 1:
                answer += cnt * (cnt-1) // 2
        
        return answer