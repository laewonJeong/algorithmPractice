class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def make_prime_num(n):
            prime = [True for i in range(n+1)]
            prime[0] = False
            if n > 0:
                prime[1] = False
            for i in range(2, int(math.sqrt(n)) + 1):
                if prime[i]:
                    j=2
                    while i * j <= n:
                        prime[i*j] = False
                        j+=1

            return prime

        prime = make_prime_num(right)
        prime_range = []
        answer = [0, 10**6]
        
        for i in range(left, right+1):
            if prime[i]:
                prime_range.append(i)
        
        if len(prime_range) < 2:
            return [-1, -1]

        for i in range(len(prime_range)-1):
            if prime_range[i+1] - prime_range[i] < answer[1] - answer[0]:
                answer[0] = prime_range[i]
                answer[1] = prime_range[i+1] 

        return answer