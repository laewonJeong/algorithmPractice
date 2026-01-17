import sys
input = sys.stdin.readline
MAX = sys.maxsize

def main():
    # Write your solution here
    n = int(input())

    if n == 1:
        print('0')
        return

    max_x = -MAX
    min_x = MAX

    max_y = -MAX
    min_y = MAX

    for _ in range(n):
        x, y = map(int, input().split())
        max_x = max(max_x, x)
        min_x = min(min_x, x)

        max_y = max(max_y, y)
        min_y = min(min_y, y)

    print((max_x - min_x) * (max_y - min_y))

if __name__ == "__main__":
    main()