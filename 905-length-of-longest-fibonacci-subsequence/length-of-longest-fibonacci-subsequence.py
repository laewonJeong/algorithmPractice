class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        arr_set = set(arr)
        start_fibo = {}
        n = len(arr)

        for i in range(n-1, 1, -1):
            for j in range(n-1 -(n-1 - i+1), -1,-1):
                if arr[i] - arr[j] >= arr[j]:
                    break           
                if arr[i] - arr[j] in arr_set: 
                    start_fibo[(arr[i] - arr[j], arr[j])] = (arr[j], arr[i])
        
        result = 0
        for k in start_fibo:
            answer = 1
            now = start_fibo[k]

            while now in start_fibo:
                now = start_fibo[now]
                answer += 1
            
            result = max(result, answer)
        
        return result+2 if result != 0 else 0