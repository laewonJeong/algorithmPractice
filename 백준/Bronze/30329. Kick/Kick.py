import sys
input = sys.stdin.readline

def main():
    # Write your solution here
    kicks = input().rstrip()
    cnt = 0

    for i in range(len(kicks)-3):
        if kicks[i:i + 4] == 'kick':
            cnt += 1

    print(cnt)

if __name__ == "__main__":
    main()