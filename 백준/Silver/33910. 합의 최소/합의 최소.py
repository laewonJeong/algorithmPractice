import sys
input = sys.stdin.readline

def main():
    # Write your solution here
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n-2, -1, -1):
        a[i] = min(a[i], a[i+1])

    print(sum(a))

if __name__ == "__main__":
    main()