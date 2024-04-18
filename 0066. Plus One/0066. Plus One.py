class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # First solution, but it doesn't work for array [9, 9] / [9, 9, 9] and so on
        # last_digit = len(digits) - 1

        # if digits[last_digit] != 9:
           # digits[last_digit] += 1
        # else:
            # digits[last_digit] = 1
            # add_digit = [0]
            # digits.extend(add_digit)
        
        # return digits

        # Here we're converting the array of digits into a single integer number
        integer_digit = int(''.join(map(str, digits)))
        # Increment the number by 1
        integer_digit += 1
        # Converting the integer number back to an array of digits
        new_digits = [int(digit) for digit in str(integer_digit)]

        return new_digits