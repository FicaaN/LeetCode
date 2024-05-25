class Solution:
    def averageValue(self, nums: List[int]) -> int:
        
        summ, counter = 0, 0

        for number in nums:
            if number % 6 == 0:
                summ += number
                counter += 1
        
        if counter == 0:
            return 0
        else:
            return summ // counter