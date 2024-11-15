class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key = lambda x:x[1], reverse = True)
        answer = []

        for query in queries:
            check = False
            for p, b in items:
                if p <= query:
                    check = True
                    answer.append(b)
                    break
            if not check:
                answer.append(0)

        return answer