from collections import defaultdict, deque
from typing import List

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        parent = list(range(n))  # 유니온 파인드용 부모 노드
        and_value = {}  # 각 연결 컴포넌트의 최소 AND 값 저장
        graph = defaultdict(list)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y, cost):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_y] = root_x
                if root_x in and_value and root_y in and_value:
                    and_value[root_x] = and_value[root_x] & and_value[root_y] & cost
                elif root_x in and_value:
                    and_value[root_x] &= cost
                elif root_y in and_value:
                    and_value[root_x] = and_value[root_y] & cost
                else:
                    and_value[root_x] = cost

        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
            union(u, v, w)

        print(and_value)

        visited = set()
        for start in range(n):
            if start not in visited:
                root = find(start)
                queue = deque([start])
                min_and = 0xFFFFFFFF

                while queue:
                    node = queue.popleft()
                    visited.add(node)
                    for neighbor, weight in graph[node]:
                        if neighbor not in visited:
                            min_and &= weight
                            queue.append(neighbor)

                and_value[root] = min(and_value.get(root, 0xFFFFFFFF), min_and)

        answer = []
        for s, t in query:
            if find(s) == find(t):
                answer.append(and_value[find(s)])
            else:
                answer.append(-1)
        return answer
