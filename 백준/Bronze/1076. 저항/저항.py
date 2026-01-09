import sys

input = sys.stdin.readline

colors = { "black":	0, "brown":	1, "red": 2, 
            "orange": 3, "yellow": 4, "green": 5, 
            "blue": 6, "violet": 7, "grey": 8, 
            "white": 9 }

def main():
    answer = 0

    for t in range(3):
        color = input().strip()
        if t == 0:
            answer += colors[color] * 10
        elif t == 1:
            answer += colors[color]
        else:
            answer *= 10 ** colors[color]
    
    print(answer)

if __name__ == "__main__":
    main()