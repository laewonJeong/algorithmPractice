W =  [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
      ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
      ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
      ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
      ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
      ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
      ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
      ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

B = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
     ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
     ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
     ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
     ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
     ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
     ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
     ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]
def r(arr,wb,x, y):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if arr[x+i][y+j] != wb[i][j]:
                cnt+=1
    #print(cnt)
    return cnt
n, m = map(int, input().split())
arr = [list(input())for _ in range(n)]
c = 64
for i in range(n-7):
    for j in range(m-7):
        w = r(arr,W,i,j)
        b = r(arr,B,i,j)
        c = min(c,w,b)
print(c)