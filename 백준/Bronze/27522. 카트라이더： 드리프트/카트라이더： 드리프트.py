import sys
input = sys.stdin.readline
PLAYERS = 8

def main():
    # Write your solution here
    red_score  = 0
    blue_score = 0
    score = [10, 8, 6, 5, 4, 3, 2, 1]

    rank = []
    for i in range(PLAYERS):
        rank.append(input().rstrip())

    rank.sort()

    for i in range(PLAYERS):
        if rank[i][-1] == 'B':
            blue_score += score[i]
        else:
            red_score  += score[i]

    print('Blue' if blue_score > red_score else 'Red')

if __name__ == "__main__":
    main()