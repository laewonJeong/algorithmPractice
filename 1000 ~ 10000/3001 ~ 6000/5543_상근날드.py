import sys

burger = []
drink =[]
for i in range(3):
    a= int(sys.stdin.readline())
    burger.append(a)
for i in range(2):
    b=int(sys.stdin.readline())
    drink.append(b)
burger = sorted(burger)
drink = sorted(drink)
print(burger[0]+drink[0]-50)