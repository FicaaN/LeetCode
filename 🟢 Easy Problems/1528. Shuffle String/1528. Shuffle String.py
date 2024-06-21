class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        new_string = ""
        indices = list(indices)
        for i in range(len(s)):
            j = indices.index(i)
            new_string += s[j]
        
        return new_string