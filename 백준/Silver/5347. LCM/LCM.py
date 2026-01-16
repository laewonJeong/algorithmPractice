import sys
import math
input = sys.stdin.readline

def main():
    # Write your solution here
    t = int(input())

    for _ in range(t):
        a, b = map(int, input().split())
        print(math.lcm(a, b))

if __name__ == "__main__":
    main()