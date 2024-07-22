class Solution:
    def minimumChairs(self, s: str) -> int:
        return max(accumulate(1 if char == 'E' else -1 for char in s))
        # we need to import accumulate for this solution
        # from itertools import accumulate
