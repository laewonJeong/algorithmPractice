import sys
input = sys.stdin.readline

def is_triangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if a + c <= b:
        return False

    return True

def main():
    # Write your solution here
    a, b, c = map(int, input().split())
    input_list = [a, b, c]
    ans = 0

    for i in range(3):
        temp = input_list[i]
        while input_list[i] != 0:
            if is_triangle(*input_list):
                ans = max(ans, sum(input_list))
                break
            input_list[i] -= 1

        input_list[i] = temp

    print(ans)

if __name__ == "__main__":
    main()