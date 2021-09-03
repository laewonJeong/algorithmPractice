import sys

n = int(sys.stdin.readline())
cnt =0
shom = 665
#print(str(n).find('666'))
while True:
    shom+=1
    if '666' in str(shom):
        cnt+=1
    if cnt == n:
        print(shom)
        break