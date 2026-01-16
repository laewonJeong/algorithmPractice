import sys
input = sys.stdin.readline
from math import gcd

def main():
    s = input().strip()

    if '.' in s:
        int_part, dec_part = s.split('.')
        dec_len = len(dec_part)
        p = int(int_part + dec_part)
        q = 10 ** dec_len
    else:
        p = int(s)
        q = 1

    divisor = gcd(p, q)
    p //= divisor
    q //= divisor

    print("YES")
    print(p, q)

if __name__ == "__main__":
    main()