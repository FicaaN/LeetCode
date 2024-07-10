class Solution:
    def reverseWords(self, s: str) -> str:
        new_s = []
        words = s.split()

        for word in words:
            word = word[::-1]
            new_s.append(word)
        
        return " ".join(new_s)

        # One liner
        # return " ".join(word[::-1] for word in s.split())