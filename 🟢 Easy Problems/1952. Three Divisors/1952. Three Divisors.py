class Solution:
    def isThree(self, n: int) -> bool:
        
        k = 0

        for i in range(1, n + 1):
            if n % i == 0:
                k += 1

        if k == 3:
            return True
        else:
            return False