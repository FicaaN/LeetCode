class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        indices = []
        i = 0

        for word in words:
            if x in word:
                indices.append(i)
            i += 1
        
        return indices