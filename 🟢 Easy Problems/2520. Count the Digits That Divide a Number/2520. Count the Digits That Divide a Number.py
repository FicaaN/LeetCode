class Solution:
    def countDigits(self, num: int) -> int:
        
        counter = 0

        digits = [int(digit) for digit in str(num)]

        for digit in digits:
            if num % digit == 0:
                counter += 1
        
        return counter