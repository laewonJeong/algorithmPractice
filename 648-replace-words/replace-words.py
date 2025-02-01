class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split()

        for root in dictionary:
            for i, word in enumerate(words):
                if word.startswith(root):
                    words[i] = root
        
        return ' '.join(words)