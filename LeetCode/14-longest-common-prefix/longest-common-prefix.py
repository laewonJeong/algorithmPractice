class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ''
        prefix = ''

        for ch in strs[0]:
            check = True
            prefix += ch

            for st in strs:
                if not st.startswith(prefix):
                    check = False
            
            if check:
                answer = prefix
        
        return answer