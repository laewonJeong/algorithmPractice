import sys
n,m=map(int,sys.stdin.readline().split())
pokemon={}
for i in range(1,n+1):
    a=sys.stdin.readline().rstrip()
    pokemon[str(i)] = a
    pokemon[a] = str(i)
for _ in range(m):
    check = sys.stdin.readline().rstrip()
    print(pokemon[check])