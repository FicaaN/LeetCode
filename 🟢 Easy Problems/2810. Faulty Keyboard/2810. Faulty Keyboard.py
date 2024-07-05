class Solution:
    def finalString(self, s: str) -> str:
        word = []
        for letter in s:
            if letter == 'i':
                word = word[::-1]
            else:
                word.append(letter)
        
        return "".join(word)