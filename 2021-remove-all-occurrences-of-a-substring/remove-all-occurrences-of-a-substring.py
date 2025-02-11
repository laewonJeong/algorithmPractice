class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while re.findall(part,s):
            s = re.sub(part,"",s,1)
            
        return s