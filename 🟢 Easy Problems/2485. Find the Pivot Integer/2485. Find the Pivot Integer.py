class Solution:
    def pivotInteger(self, n: int) -> int:
        
        numbers = []

        for i in range(1, n + 1):
            numbers.append(i)
        
        for number in range(n):
            beforeSum = sum(numbers[:number + 1])
            afterSum = sum(numbers[number:])

            if beforeSum == afterSum:
                return number + 1
        
        return -1