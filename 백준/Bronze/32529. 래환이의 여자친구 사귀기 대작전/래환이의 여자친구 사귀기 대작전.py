import sys
input = sys.stdin.readline

def main():
    # Write your solution here
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    if sum(a) < m:
        print("-1")
        return

    temp = 0
    for i in range(n - 1, -1, -1):
        temp += a[i]
        if temp >= m:
            print(i + 1)
            break

    return

if __name__ == "__main__":
    main()