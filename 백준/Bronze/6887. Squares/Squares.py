import sys
import math
input = sys.stdin.readline

def main():
    # Write your solution here
    tiles = int(input())
    side = int(math.sqrt(tiles))

    print(f'The largest square has side length {side}.')

if __name__ == "__main__":
    main()