def quad_zip(arr, len_arr):
    new_arr, n = [], len_arr//2
    for i in range(1,3):
        new_arr.append([arr[j][n*(i-1):n*i] for j in range(len_arr)])
    return [new_arr[0][0:n], new_arr[0][n:], new_arr[1][0:n], new_arr[1][n:]]

def recursion(zero, one, arr):
    if sum([ar.count(0) for ar in arr]) == 0: return zero, one+1
    elif sum([ar.count(1) for ar in arr]) == 0: return zero+1, one
    else:
        arr = quad_zip(arr, len(arr))
        for i in range(4):
            zero, one = recursion(zero, one, arr[i])
    return zero, one

def solution(arr):
    zero, one = 0, 0

    return recursion(zero, one, arr)
