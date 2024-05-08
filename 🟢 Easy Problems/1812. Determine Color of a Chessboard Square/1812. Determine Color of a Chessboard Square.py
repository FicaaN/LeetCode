class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        
        letters = {"a", "c", "e", "g"}

        if int(coordinates[1]) % 2 == 0:
            if coordinates[0] in letters:
                return True
            else:
                return False
        else:
            if coordinates[0] in letters:
                return False
            else:
                return True