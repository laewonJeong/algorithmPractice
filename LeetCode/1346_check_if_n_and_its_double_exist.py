class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
	double_arr = defaultdict(list)

        for i, num in enumerate(arr):
            double_arr[2 * arr[i]].append(i)

        for i, num in enumerate(arr):
            if num in double_arr and double_arr[num] != [i]:
                return True
        
        return False
