import sys
input = sys.stdin.readline

def main():
    # Write your solution here
    money = int(input())
    watermelon = int(input())
    pomegranates = int(input())
    nuts = int(input())

    answer = 'Nothing'
    if money >= watermelon:
        answer = 'Watermelon'
    elif money >= pomegranates:
        answer = 'Pomegranates'
    elif money >= nuts:
        answer = 'Nuts'

    print(answer)

if __name__ == "__main__":
    main()