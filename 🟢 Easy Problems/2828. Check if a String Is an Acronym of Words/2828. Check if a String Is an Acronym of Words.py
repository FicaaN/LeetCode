class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        letters = ''.join(word[0] for word in words)
        return letters == s
