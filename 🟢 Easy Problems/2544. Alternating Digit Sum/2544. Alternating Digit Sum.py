class Solution:
    def alternateDigitSum(self, n: int) -> int:
        
        str_n = str(n)
        sum = 0

        for i in range(len(str_n)):
            digit = int(str_n[i])
            if i % 2 == 0:
                sum += digit
            else:
                sum -= digit

        return sum