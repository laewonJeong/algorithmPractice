import sys
from collections import deque
s=deque()
a = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()
check=0
for i in a:
    s.appendleft(i) #스택에 문자열 하나씩 넣음
    if i == bomb[-1]: #만약 이번 문자가 폭탄의 마지막 문자면
        if len(s) < len(bomb): # 근데 만약 스택 길이보다 폭탄길이가 크면
            temp =1 #아무일도 일어나지 않았다
        else: #스택길이가 폭탄길이보다 크면
            x = len(bomb)-2
            for j in range(1,len(bomb)): #폭탄길이만큼 비교
                if bomb[x] == s[j]: #만약 폭탄이랑 스택에 있는 값이 같으면
                    check +=1 #check + 1
                    x-=1
            if check == len(bomb)-1: #만약 check값이 폭탄길이와 같으면
                for i in range(len(bomb)):
                    s.popleft()#폭탄길이만큼 스택에서 빼준다
    check = 0
if len(s) == 0:
    print('FRULA')
else:
    s.reverse()
    for i in s:
        print(i,end='')