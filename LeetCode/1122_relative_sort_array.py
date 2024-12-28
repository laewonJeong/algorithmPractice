class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr = []
        n = len(arr2)

        arr2_with_idx = {k:v for v, k in enumerate(arr2)}

        for num in arr1:
            if num in arr2_with_idx:
                arr.append((arr2_with_idx[num], num))
            else:
                arr.append((n, num))
        
        arr.sort(key = lambda x:(x[0], x[1]))

        return [num for _, num in arr]
