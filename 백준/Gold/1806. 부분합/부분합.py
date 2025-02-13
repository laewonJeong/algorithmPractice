import sys
input = sys.stdin.readline

n, s = map(int, input().split())

arr = list(map(int, input().split()))

if sum(arr) < s:
    print(0)
    sys.exit()

left = 0
right = 0
sum = arr[0]
ans = float('inf')

while left <= right and right < n:
    if sum < s:
        right += 1
        if right < n:
            sum += arr[right]
    elif sum == s:
        ans = min(ans, right - left + 1)
        left += 1
        sum -= arr[left - 1]
    else:
        ans = min(ans, right - left + 1)
        sum -= arr[left]
        left += 1

print(ans)