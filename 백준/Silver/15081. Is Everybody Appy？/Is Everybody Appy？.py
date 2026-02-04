import sys
input = sys.stdin.readline

def main():
    # Write your solution here
    n = int(input())
    check = set()
    answer = []

    for _ in range(n):
        apps = input().split()
        for i in range(1, len(apps)):
            app = apps[i]
            if app not in check:
                answer.append(app)
                check.add(app)
                break

    print(*answer)

if __name__ == "__main__":
    main()