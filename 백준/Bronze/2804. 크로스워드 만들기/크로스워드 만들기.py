import sys
input = sys.stdin.readline

def main():
    # Write your solution here
    A, B   = input().rstrip().split()
    N, M   = len(A), len(B)
    answer = [['.' for _ in range(N)] for _ in range(M)]
    cross  = [-1, -1]

    for i in range(N):
        for j in range(M):
            if A[i] == B[j]:
                cross = [i, j]
                break
        if cross[0] != -1:
            break

    answer[cross[1]] = list(A)
    for i in range(M):
        answer[i][cross[0]] = B[i]
        print(''.join(answer[i]))


if __name__ == "__main__":
    main()