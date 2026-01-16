import sys
input = sys.stdin.readline

def main():
    need_del = set(input().strip())
    text = list(input().strip())

    result = [c for c in text if c not in need_del]

    print(''.join(result))

if __name__ == "__main__":
    main()