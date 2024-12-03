class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        s = list(s)

        for space in spaces:
            s[space] = f' {s[space]}'
        
        return ''.join(s)
