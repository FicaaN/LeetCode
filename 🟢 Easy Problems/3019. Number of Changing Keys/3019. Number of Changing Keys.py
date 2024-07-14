class Solution:
    def countKeyChanges(self, s: str) -> int:
        counter = 0
        s = s.lower()
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                counter += 1
        
        return counter