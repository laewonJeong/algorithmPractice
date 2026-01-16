import sys
input = sys.stdin.readline

def main():
    while True:
        line = input().rstrip()
        if line == "END":
            break
        print(line[::-1])

if __name__ == "__main__":
    main()