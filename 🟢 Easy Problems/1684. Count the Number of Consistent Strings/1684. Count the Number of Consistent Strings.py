class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        counter = 0
        allowed_set = set(allowed)

        for word in words:
            if all(char in allowed_set for char in word):
                counter += 1
        
        return counter

        # return sum(all(char in allowed_set for char in word) for word in words)