class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        def find(parent, x):
            if parent[x] != x:
                parent[x] = find(parent, parent[x])
            return parent[x]
        
        def union(parent, rank, x, y):
            root_x = find(parent, x)
            root_y = find(parent, y)
            
            if root_x != root_y:
                if rank[root_x] > rank[root_y]:
                    parent[root_y] = root_x
                elif rank[root_x] < rank[root_y]:
                    parent[root_x] = root_y
                else:
                    parent[root_y] = root_x
                    rank[root_x] += 1
        
        parent = list(range(n))
        rank = [0] * n
        edge_count = defaultdict(int)
        node_count = defaultdict(int)

        for v1, v2 in edges:
            union(parent, rank, v1, v2)
        
        for i in range(n):
            root = find(parent, i)
            node_count[root] += 1

        for v1, v2 in edges:
            root = find(parent, v1)
            edge_count[root] += 1  

        answer = 0
        for root in node_count:
            k = node_count[root]
            expected_edges = k * (k - 1) // 2
            if edge_count[root] == expected_edges:
                answer += 1
        
        return answer
