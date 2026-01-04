import sys

def main():
    p_nums = sys.stdin.readline().split()
    prefix = sys.stdin.readline().rstrip()
    ans = 0

    for p_num in p_nums:
        if p_num.startswith(prefix) and p_num != prefix:
            ans += 1

    return ans

if __name__ == "__main__":
    print(main())