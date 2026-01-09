class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()

        answer = [folder[0] + '/']

        for i in range(1, len(folder)):
            if folder[i].startswith(answer[-1]):
                continue
            else:
                answer.append(folder[i] + '/')
        
        return [a[:-1] for a in answer]