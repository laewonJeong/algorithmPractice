def find(parent, x):
	if parent[x] == x:
		return x
	parent[x] = find(parent, parent[x])
	return parent[x]

def union(parent, a, b):
	rootA = find(parent, a)
	rootB = find(parent, b)
	if rootA < rootB:
		parent[rootB] = rootA
	else:
		parent[rootA] = rootB

def solution(n, costs):
    parent = [0] * (n + 1)

    edges = []
    result = 0

    for i in range(1, n + 1):
        parent[i] = i
        
    costs.sort(key = lambda x:x[2])
    
    for cost in costs:
        a, b, c = cost
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            result += c

    return result
