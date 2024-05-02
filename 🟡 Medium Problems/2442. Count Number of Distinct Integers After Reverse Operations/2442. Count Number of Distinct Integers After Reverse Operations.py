class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        new_nums = []

        for number in nums:
            new_nums.append(int(str(number)[::-1]))
        
        nums += new_nums

        # set(nums) is used to create a set of unique elements from the nums
        return len(set(nums))