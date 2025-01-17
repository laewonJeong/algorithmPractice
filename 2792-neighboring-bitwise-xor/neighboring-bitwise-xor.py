class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        original = [0]
        n = len(derived)

        for i in range(1, n):
            if derived[i-1] == 1:
                if original[i-1] == 0:
                    original.append(1)
                else:
                    original.append(0)
            else:
                if original[i-1] == 0:
                    original.append(0)
                else:
                    original.append(1)
        
        return original[-1] ^ original[0] == derived[-1]
            
