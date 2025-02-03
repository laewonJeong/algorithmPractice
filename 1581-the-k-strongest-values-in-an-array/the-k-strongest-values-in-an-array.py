class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        median = arr[(n-1)//2]

        arr.sort(key = lambda x:(abs(x - median), x))
  
        return arr[n-k:]