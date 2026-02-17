import sys
input = sys.stdin.readline

def main():
    s = input().rstrip()

    inner = s[1:-1]
    if s[0] == '"' and s[-1] == '"' and inner.strip():
        print(inner)
    else:
        print("CE")

if __name__ == "__main__":
    main()