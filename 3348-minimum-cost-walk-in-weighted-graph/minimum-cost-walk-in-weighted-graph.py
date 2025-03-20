class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        and_result = [-1] * n

        def find(parent, x):
            if parent[x] != x:
                parent[x] = find(parent, parent[x])
            return parent[x]

        def union(parent, x, y, cost):
            root_x = find(parent, x)
            root_y = find(parent, y)
            and_result[root_x] &= cost & and_result[root_y]
            and_result[root_y] = and_result[root_x]

            if root_x < root_y:
                parent[root_y] = root_x
            else:
                parent[root_x] = root_y
           
        
        parent = list(range(n))

        for v1, v2, cost in edges:
            union(parent, v1, v2, cost)
        
        answer = []
        for v1, v2 in query:
            root_x = find(parent, v1)
            root_y = find(parent, v2)

            if root_x == root_y:
                answer.append(and_result[root_x])
            else:
                answer.append(-1)
        
        return answer