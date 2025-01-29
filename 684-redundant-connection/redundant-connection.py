def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)

    if root_a == root_b:
        return False
    else:
        parent[root_a] = root_b
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}

        for v1, v2 in edges:
            if v1 not in parent:
                parent[v1] = v1
            if v2 not in parent:
                parent[v2] = v2

            if not union(parent, v1, v2):
                return [v1, v2]
        