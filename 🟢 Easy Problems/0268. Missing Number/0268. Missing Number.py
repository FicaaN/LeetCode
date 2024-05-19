class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        n_sum = n * (n + 1) // 2
        nums_sum = sum(nums)

        return n_sum - nums_sum