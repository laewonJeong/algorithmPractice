def solution(diffs, times, limit):
    answer = 0
    n = len(diffs)
    
    left, right = 0, 3000001
    while left <= right:
        mid = (left+right)//2
        check_time = 0
        i = mid
        for j in range(n):
            if diffs[j] > i:
                if j == 0:
                    check_time += (times[j]) * (diffs[j] - i)
                else:
                    check_time += (times[j]) + (times[j-1] + times[j]) * (diffs[j]-i)
            else:
                check_time += times[j]
            
        if check_time > limit:
            left = mid + 1
        else:
            right = mid - 1
    
    return left if left != 0 else 1