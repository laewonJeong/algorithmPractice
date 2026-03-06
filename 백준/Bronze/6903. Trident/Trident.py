import sys
input = sys.stdin.readline

def main():
    # Write your solution here
    t = int(input())
    s = int(input())
    h = int(input())

    for _ in range(t):
        print("*" + " " * s, end='')
        print("*" + " " * s, end='')
        print("*")

    print('*' * (s * 2 + 3))

    for _ in range(h):
        print(" " * (s + 1) + "*")

if __name__ == "__main__":
    main()