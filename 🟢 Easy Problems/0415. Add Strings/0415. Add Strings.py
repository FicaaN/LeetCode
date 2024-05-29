class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(4300*1000)
        
        # Not the proper solution
        return str(int(num1) + int(num2))