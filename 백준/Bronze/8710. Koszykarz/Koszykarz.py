import sys
input = sys.stdin.readline

def main():
    k, w, m = map(int, input().split())

    if k >= w:
        print(0)
    else:
        ans = (w - k + m - 1) // m
        print(ans)

if __name__ == "__main__":
    main()