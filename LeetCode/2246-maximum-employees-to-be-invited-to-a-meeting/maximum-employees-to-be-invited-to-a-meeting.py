class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        in_degree = [0 for _ in range(n)]
        chain = [1 for _ in range(n)]
        visited = [False for _ in range(n)]

        for i in range(n):
            in_degree[favorite[i]] += 1
        
        q = deque([])
        for i in range(n):
            if in_degree[i] == 0:
                q.append(i)

        while q:
            vertex = q.popleft()
            visited[vertex] = True
            n_vertex = favorite[vertex]
            chain[n_vertex] = max(chain[n_vertex], chain[vertex] + 1)
            in_degree[n_vertex] -= 1
            if in_degree[n_vertex] == 0:
                q.append(n_vertex)
        
        cycle = 0
        two_cycle = 0

        for i in range(n):
            if visited[i]:
                continue
            vertex = i
            cycle_len = 0
            while not visited[vertex]:
                visited[vertex] = True
                cycle_len += 1
                vertex = favorite[vertex]    
            
            if cycle_len == 2:
                two_cycle += chain[vertex] + chain[favorite[vertex]]
            else:
                cycle = max(cycle, cycle_len)
        
        return max(cycle, two_cycle)