import sys
input = sys.stdin.readline

def main():
    # Write your solution here
    people = int(input())

    three = 0
    two = 0

    while people >= 3:
        people -= 3
        three += 1

    if people == 1:
        three -= 1
        two += 2
    elif people == 2:
        two += 1

    print(f'{two} {three}')

if __name__ == "__main__":
    main()