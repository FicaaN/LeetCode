class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        
        # This sums up every number in nums list
        element_sum = sum(nums)

        # Firstly, we iterate over each number in nums array (for number in nums)
        # Then, we convert number to string (str(number)), and iterate over each digit in number (for digit in str(number))
        # (int(digit)) converts back the string digit to a integer digit
        digit_sum = sum(int(digit) for number in nums for digit in str(number))

        return abs(element_sum - digit_sum)