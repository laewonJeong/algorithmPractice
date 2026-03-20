import sys
input = sys.stdin.readline

def main():
    # Write your solution here

    week = 1
    while True:
        n = int(input())
        if not n:
            break

        s = set()
        for _ in range(n):
            s.add(input().rstrip())

        print(f'Week {week} {len(s)}')

        week+= 1

if __name__ == "__main__":
    main()