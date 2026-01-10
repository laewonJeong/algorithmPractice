import sys
input = sys.stdin.readline

def put_bottle(n: int, m: str, d: str) -> str:
    if m == d:
        return "Good"

    m_bottle_cnt = m.count('w')
    d_bottle_cnt = d.count('w')

    if m_bottle_cnt > d_bottle_cnt:
        return "Oryang"
    elif m_bottle_cnt < d_bottle_cnt:
        return "Manners maketh man"

    return "Its fine"

if __name__ == "__main__":
    n       = int(input())
    morning = input()
    dinner  = input()

    print(put_bottle(n, morning, dinner))