import sys

input = sys.stdin.readline

def main():
    n = int(input())

    for _ in range(n):
        exp = input()
        print(eval(exp) if '+' in exp else "skipped")

if __name__ == "__main__":
    main()