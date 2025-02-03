class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        sorted_arr = sorted(arr)
        n = len(arr)
        median = sorted_arr[(n-1)//2]

        new_arr = []
        for i in range(n):
            new_arr.append((abs(arr[i] - median), arr[i]))
        
        new_arr.sort(reverse = True)

        answer = []

        for i in range(k):
            answer.append(new_arr[i][1])
        
        return answer