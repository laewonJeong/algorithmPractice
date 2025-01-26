import sys

def bellman_ford(graph, start,n):
    distance=[2200000000]*(n+1)
    distance[start] = 0
    result = False
    for _ in range(1,n+1):
        for i in range(1,n+1):
            for j,k in graph[i]:
                dis = distance[i]+k
                if(distance[j] > dis):
                    distance[j] = dis
                    if _ == n:
                        result = True
    return distance,result

testcase = int(sys.stdin.readline())
for _ in range(testcase):
    n,m,w = map(int,sys.stdin.readline().split())
    graph=[[] for j in range(n+1)]
    for i in range(m):
        s,d,we = map(int,sys.stdin.readline().split())
        graph[s].append([d,we])
        graph[d].append([s,we])
    for i in range(w):
        s,d,we = map(int,sys.stdin.readline().split())
        graph[s].append([d,-we])
    a,b=bellman_ford(graph,1,n)
    if a[1] <0 or b==True:
        print('YES')
    else:
        print('NO')