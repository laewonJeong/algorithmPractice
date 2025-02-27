class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        arr_dic = defaultdict(bool)
        start_fibo = defaultdict(int)
        n = len(arr)
        for num in arr:
            arr_dic[num] = True

        key = []
        for i in range(n-1, 1, -1):
            for j in range(n-1 -(n-1 - i+1), -1,-1):
                if arr[i] - arr[j] >= arr[j]:
                    break           
                if arr_dic[arr[i] - arr[j]]: 
                    start_fibo[(arr[i] - arr[j], arr[j])] = (arr[j], arr[i])
                    key.append((arr[i] - arr[j], arr[j]))
        
        result = 0
        for k in key:
            answer = 1
            now = start_fibo[k]
            while True:
                if start_fibo[now] == 0:
                    break
                else:
                    now = start_fibo[now]
                    answer += 1
            
            result = max(result, answer)
        
        return result+2 if result != 0 else 0