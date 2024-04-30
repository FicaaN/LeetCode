class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        running_sum = 0
        result = []

        for number in nums:
            running_sum += number
            result.append(running_sum)
        
        return result