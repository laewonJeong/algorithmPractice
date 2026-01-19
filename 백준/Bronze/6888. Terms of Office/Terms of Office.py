# Terms of Office
import sys
input = sys.stdin.readline

def main():
    # Write your solution here
    x = int(input())
    y = int(input())

    while x <= y:
        print(f'All positions change in year {x}')
        x += 60

if __name__ == "__main__":
    main()