import sys

input = sys.stdin.readline

def main():
    loc_a, loc_b = map(int, input().split())
    loc_a -= 1
    loc_b -= 1
    
    row_dis = abs(loc_a // 4 - loc_b // 4)
    col_dis = abs(loc_a % 4 - loc_b % 4)

    print(row_dis + col_dis)

if __name__ == "__main__":
    main()