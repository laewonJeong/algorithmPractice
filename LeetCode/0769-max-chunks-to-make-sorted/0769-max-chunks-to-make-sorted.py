class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        answer = 0
        arr_permutation = ["0" for _ in range(n)]
        
        for i in range(1, n):
            arr_permutation[i] = arr_permutation[i-1]+str(i)

        now_permutation = ["11" for _ in range(n)]
        for i in range(n):
            now_permutation[arr[i]] = str(arr[i])
            if ''.join(now_permutation[:i+1]) == arr_permutation[i]:
                answer += 1

        return answer