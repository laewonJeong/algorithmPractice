def solution(N, number):
    if number == N:
        return 1
    
    dp = [set() for _ in range(8)]
    dp[0].add(N)
    #dp[1].add(N+N)
    #dp[1].add(N-N)
    #dp[1].add(N//N)
    #dp[1].add(N*N)
    #dp[1].add(N*10 + N)
    
    #if number in dp[1]:
    #    return 2
    
    for i in range(1, 8):
        dp[i].add(int(str(N) * (i+1)))
        for j in range(i):
            for num1 in dp[j]:
                for num2 in dp[i-j-1]:
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    
                    if num2 != 0:
                        dp[i].add(num1 // num2)
                
                    dp[i].add(num1 * num2)
                    
        if number in dp[i]:
            return i+1
            
    return -1