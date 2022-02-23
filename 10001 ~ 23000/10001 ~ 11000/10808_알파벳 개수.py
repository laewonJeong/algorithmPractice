alpha = [0 for i in range(26)]
s = input()
for i in s:
        alpha[ord(i)-97]+=1
for i in alpha:
        print(i,end=" ")
