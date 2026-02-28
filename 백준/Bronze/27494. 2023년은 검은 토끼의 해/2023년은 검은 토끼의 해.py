import sys
input = sys.stdin.readline

def main():
    # Write your solution here
    n = int(input())

    if n < 2023:
        print(0)
        return

    answer = 1
    want = '2023'

    for i in range(2024, n + 1):
        want_idx = 0
        for num in str(i):
            if num == want[want_idx]:
                want_idx += 1
            if want_idx == 4:
                answer += 1
                break

    print(answer)

if __name__ == "__main__":
    main()