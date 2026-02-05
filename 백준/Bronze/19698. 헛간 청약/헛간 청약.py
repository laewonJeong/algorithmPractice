import sys
input = sys.stdin.readline

def main():
    # Write your solution here
    n, w, h, l = map(int, input().split())

    a = (w//l) * (h//l)

    print(min(a, n))

if __name__ == "__main__":
    main()