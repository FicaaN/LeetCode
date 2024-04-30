class Solution:
    def maximum69Number (self, num: int) -> int:
        
        # Converting number to a list of digits
        digits = [int(digit) for digit in str(num)]

        # Iteration through each digit
        for i in range(len(digits)):
            if digits[i] == 6:
                digits[i] = 9
                break
        
        # Converting the list of digits back to integer
        return int(''.join(map(str, digits)))