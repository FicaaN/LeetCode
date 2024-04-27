class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        def is_self_dividing(num: int) -> bool:
            digits = [int(digit) for digit in str(num)]

            for digit in digits:
                if digit == 0 or num % digit != 0:
                    return False
            
            return True
        
        result = []
        for number in range(left, right + 1):
            if is_self_dividing(number):
                result.append(number)
        
        return result