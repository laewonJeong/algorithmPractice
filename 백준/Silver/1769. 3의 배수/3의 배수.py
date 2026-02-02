import sys
input = sys.stdin.readline

def main():
    # Write your solution here
    x = input().rstrip()
    if len(x) == 1:
        print(0)
        print("NO" if int(x) % 3 != 0 else "YES")
        return

    cnt = 1
    while True:
        temp = 0
        for num in x:
            temp += int(num)

        if len(str(temp)) != 1:
            x = str(temp)
        else:
            break
        cnt += 1

    print(cnt)
    print("NO" if temp % 3 != 0 else "YES")



if __name__ == "__main__":
    main()