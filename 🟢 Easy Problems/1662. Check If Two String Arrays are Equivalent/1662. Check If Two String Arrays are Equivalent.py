class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        first_word = "".join([word for word in word1])
        second_word = "".join([word for word in word2])

        return first_word == second_word