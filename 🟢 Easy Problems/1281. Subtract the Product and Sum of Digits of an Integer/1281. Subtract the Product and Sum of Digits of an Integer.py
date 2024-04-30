class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        # Firstly, we convert the integer to a string, because it's easier to find digits
        digits = [int(digit) for digit in str(n)]

        # Here we find the product of digits
        digit_product = 1
        for digit in digits:
            digit_product *= digit
        
        # And here we find the sum of digits 
        digit_sum = sum(digits)

        return digit_product - digit_sum