class Solution:
    def isFascinating(self, n: int) -> bool:
        
        number = str(n) + str(n * 2) + str(n * 3)

        if len(number) != 9 or '0' in number:
            return False
        
        number_set = set(number)

        return number_set == set('123456789')