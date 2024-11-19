import sys

a=int(sys.stdin.readline())
cnt = 0
checking = 0
for j in range(a):
    check = [0]*26
    group_word = sys.stdin.readline()
    for i in range(len(group_word)-1):
        if group_word[i] == group_word[i+1]:
            continue
        else:
            if check[ord(group_word[i])-97] == 0:
                check[ord(group_word[i])-97] = 1
            else:
                checking = 1
                break
    if(checking == 0):
        cnt+=1
    else:
        checking = 0
    
print(cnt)