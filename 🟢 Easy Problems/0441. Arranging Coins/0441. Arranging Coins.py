class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        complete_rows = 0
        current_row = 1

        while n >= current_row:
            n -= current_row
            current_row += 1
            complete_rows += 1
        
        return complete_rows