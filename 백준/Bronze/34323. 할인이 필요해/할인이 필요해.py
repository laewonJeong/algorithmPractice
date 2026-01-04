import sys

def need_discount():
    n, m, s = map(int, sys.stdin.readline().split())

    n_discount = s * (m + 1) * (100 - n) // 100 #(s - (s * n/100)) * (m+1)
    m_discount = s * m

    return min(n_discount, m_discount)

if __name__ == "__main__":
    print(int(need_discount()))